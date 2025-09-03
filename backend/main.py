from email.mime import image
import subprocess
import sys
from typing_extensions import Self
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator
from typing import Annotated, Any
# from tensorflow.keras.models import load_model
from PIL import Image
import io
import os
from tensorflow import keras
import numpy as np




app=FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class UserInfo(BaseModel):
    mobile_number: Annotated[str, Field(max_length=10, min_length=10)]
    password: Annotated[str, Field(min_length=8)]
    latitude: float
    longitude: float
    
    @field_validator("mobile_number")
    @classmethod
    def mobile_number_validation(cls, value):
        if not value.isdigit():
            raise ValueError("Mobile number must be numeric")
        return value


#Loading the model
model=keras.models.load_model("D:\\DL\\ImageClassification\\RoadClassifier\\deployment_models\\pothole_detector_vgg_20250803_124150.keras")

@app.get("/")
def read_root():
    return{"message":"Automatic Road Complaint and Identifier API"}

@app.get("/about")
def read_about():
    return{"message":"Enables users to report road issues automatically "}

@app.post("/user")
async def create_user(
    mobile_number: str = Form(...),
    password: str = Form(...),
    latitude: float = Form(...),
    longitude: float = Form(...),
    image: UploadFile = File(...)
):
    script_path = os.path.join(os.path.dirname(__file__), "..", "Playwright", "codegen_complain.py")

    cmd = [
        sys.executable, script_path,
        "--mobile", mobile_number,
        "--password", password,
        "--lat", str(latitude),
        "--lon", str(longitude)
    ]
    print("Running command:", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

    # Validate mobile number
    if len(mobile_number) != 10 or not mobile_number.isdigit():
        return JSONResponse(status_code=400, content={"message": "Mobile number must be 10 digits"})
    
    # Validate password
    if len(password) < 8:
        return JSONResponse(status_code=400, content={"message": "Password must be at least 8 characters"})
    
    # Validate image file type and process image
    try:
        # Check if filename exists
        if not image.filename:
            return JSONResponse(status_code=400, content={"message": "No filename provided for image"})
        
        # Validate image file type
        if not image.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            return JSONResponse(status_code=400, content={"message": "Invalid image format. Please upload PNG, JPG, JPEG, GIF, or BMP files."})
        
        # Read image content to validate it's a valid image
        image_content = await image.read()
        try:
            img = Image.open(io.BytesIO(image_content))
            img.verify()  # Verify it's a valid image
        except Exception as e:
            return JSONResponse(status_code=400, content={"message": f"Invalid image file: {str(e)}"})
        
        image_data = {
            "filename": image.filename,
            "content_type": image.content_type,
            "size": len(image_content)
        }
    except Exception as e:
        return JSONResponse(status_code=400, content={"message": f"Error processing image: {str(e)}"})

    user_data = {
        "mobile_number": mobile_number,
        "password": password,
        "latitude": latitude,
        "longitude": longitude,
        "image_info": image_data
    }
    return JSONResponse(status_code=201, content={"message": "Records taken successfully"})

@app.post("/predict")
async def predict_image(image: UploadFile = File(...)):
    import uuid

    UPLOAD_DIR = "uploads"
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Create unique filename
    if not image.filename:
        file_ext = ".jpg"  # Default extension
    else:
        file_ext = os.path.splitext(image.filename)[1]
        if not file_ext:
            file_ext = ".jpg"  # Default extension if no extension found
    
    file_name = f"{uuid.uuid4()}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, file_name)
    pdf_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.pdf")

    # Save uploaded file to disk
    with open(file_path, "wb") as f:
        f.write(await image.read())

    # Load and preprocess image
    target_size = (224, 224)
    img = Image.open(file_path).convert("RGB").resize(target_size)

    # Convert to array and normalize
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction
    if model is None:
        return JSONResponse(status_code=500, content={"message": "AI model not loaded"})
    
    predictions = model.predict(img_array)
    prediction = predictions[0][0]

    # Interpret result
    if prediction > 0.5:
        result = "Pothole Detected"
        confidence = float(prediction)
    else:
        result = "Normal Road"
        confidence = float(1 - prediction)

    return JSONResponse(
        status_code=200,
        content={
            "result": result,
            "confidence": confidence,
            "pdf_path": pdf_path
        }
    )
