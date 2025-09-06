# 🛣️ StreetVision: AI-Powered Road Complaint Automation

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg?style=flat&logo=FastAPI)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat&logo=python)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.10.0-FF6F00.svg?style=flat&logo=tensorflow)](https://tensorflow.org)
[![Netlify](https://img.shields.io/badge/Netlify-Deployed-00C7B7?style=flat&logo=netlify)](https://streetvision.netlify.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🚀 Project Overview

StreetVision is a full-stack, agentic platform for intelligent road monitoring and automated pothole complaint submission. It leverages deep learning, web automation, and modern frontend design to empower citizens to report road issues efficiently and reliably.

---

## 🎯 Problem Statement & Usefulness

Potholes and road defects are a major public safety concern, often underreported due to cumbersome complaint processes. StreetVision solves this by:
- **Automating the complaint filing process** to government portals (CGPRAMS/PG Portal)
- **Empowering users** to submit evidence (photo, location) with minimal effort
- **Ensuring reliability** by keeping the human in the loop for CAPTCHA solving
- **Providing instant AI analysis** of road images for actionable feedback

---

## 🧑‍💻 How It Works

1. **User uploads a road image** (pothole evidence)
2. **Enters mobile number and password** (for CGPRAMS portal)
3. **Analyzes the image** using AI-powered detection
4. **Submits the report** – the agentic backend automates the official complaint filing, pausing for human CAPTCHA input
5. **Location is validated** via GPS and Google Maps integration

---

## 🛠️ Tech Stack

### **Backend Technologies**
- **FastAPI 0.104.1** - Modern, high-performance async web framework
- **TensorFlow 2.10.0** - Deep learning model inference and processing
- **Playwright 1.40.0** - Browser automation for government portal interaction
- **Pydantic 2.5.0** - Data validation and serialization
- **Uvicorn** - ASGI server for production deployment

### **Frontend Technologies**
- **HTML5** - Semantic markup and structure
- **CSS3** - Advanced styling with gradients, animations, and responsive design
- **Vanilla JavaScript** - Async API calls, DOM manipulation, and user interactions
- **Modern UI/UX** - Interactive components with loading states and feedback

### **Machine Learning & AI**
- **Custom CNN Model** - Built from scratch with 94% accuracy
- **VGG Transfer Learning** - Pre-trained model with 96% reliability
- **Keras/TensorFlow** - Model training, evaluation, and deployment
- **NumPy** - Numerical computing and array operations
- **Pillow (PIL)** - Image processing and manipulation

> **⚠️ Important Note on TensorFlow Version:**
> This project uses TensorFlow 2.10.0 for compatibility with older systems. However, for deployment on modern hosting platforms (Render, Heroku, AWS, etc.), we **strongly recommend using TensorFlow 2.12+ or the latest stable version** as older versions may face compatibility issues with cloud deployment environments.
> 
> If you successfully deploy this project with newer TensorFlow versions, please reach out - we'd love to hear about your experience and update our deployment guides!

### **Data & Image Processing**
- **EXIF Data Extraction** - GPS coordinates from image metadata
- **Image Preprocessing** - Resizing, normalization, and augmentation
- **Geospatial Integration** - Location services and reverse geocoding
- **File Handling** - Multi-format image upload and validation

### **Automation & Integration**
- **Playwright Automation** - Headless browser control
- **Government Portal APIs** - CGPRAMS/PG Portal integration
- **HTTP Requests** - RESTful API communication
- **Form Automation** - Dynamic form filling and submission

### **Development & Deployment**
- **Python 3.8+** - Core programming language
- **Git Version Control** - Source code management
- **Netlify** - Frontend deployment and hosting
- **Environment Variables** - Configuration management
- **CORS Middleware** - Cross-origin resource sharing

### **Libraries & Dependencies**
```python
# Core Framework
fastapi==0.104.1
uvicorn[standard]==0.24.0

# Machine Learning
tensorflow==2.10.0
numpy==1.21.6
Pillow==10.1.0

# Automation
playwright==1.40.0
requests==2.31.0

# Data Validation
pydantic==2.5.0
python-multipart==0.0.6

# Development Tools
pytest==7.4.3
black==23.11.0
python-dotenv==1.0.0
```

---

## 🏆 Key Learnings & Technologies

- **FastAPI**: Built a robust, async backend API for image analysis and automation
- **Playwright Automation**: Automated government portal navigation and form filling, with agentic design (human-in-the-loop for CAPTCHA)
- **Frontend Engineering**: Designed a beautiful, responsive UI deployed on Netlify
- **GRPSpatial Location**: Used Pillow for image handling and integrated geospatial location via Google Maps
- **Custom CNN Model**: Engineered a custom convolutional neural network achieving **94% test accuracy**, on par with pre-trained models
- **Model Selection**: Chose VGG for deployment due to its industry trust and reliability (**96% accuracy**)
- **Deployment**: Frontend live on Netlify, backend ready for local development

---

## 🧠 AI Model Highlights

- **Custom CNN**: Lightweight, efficient, and highly accurate (94% test accuracy)
- **VGG Model**: Deployed for its proven reliability, transparency, and 96% accuracy
- **Model Comparison**: Custom CNN matched VGG performance, but VGG chosen for trust in real-world deployment

---

## 🌐 Demo Video


https://github.com/user-attachments/assets/12de99b7-e9c9-4c00-b176-df295de1b084



---

## 🖥️ Project Architecture

### **System Architecture**
```
StreetVision Platform
├── 🎨 Frontend Layer (Netlify)
│   ├── HTML5 + CSS3 + JavaScript
│   ├── Responsive UI Components
│   ├── Real-time User Feedback
│   └── Google Maps Integration
│
├── 🚀 Backend API (FastAPI)
│   ├── RESTful Endpoints (/predict, /user)
│   ├── File Upload Handling
│   ├── Data Validation (Pydantic)
│   └── CORS Middleware
│
├── 🧠 AI Engine (TensorFlow)
│   ├── Custom CNN Model (94% accuracy)
│   ├── VGG Transfer Learning (96% accuracy)
│   ├── Image Preprocessing Pipeline
│   └── Prediction & Confidence Scoring
│
├── 🤖 Automation Layer (Playwright)
│   ├── Browser Automation
│   ├── Government Portal Navigation
│   ├── Form Auto-filling
│   └── Human-in-Loop CAPTCHA
│
└── 🌍 Geospatial Services
    ├── EXIF GPS Extraction
    ├── Manual Location Picker
    ├── Reverse Geocoding
    └── Location Validation
```

### **Data Flow**
1. **Image Upload** → Frontend validates → Sends to Backend
2. **AI Processing** → TensorFlow model analyzes → Returns prediction
3. **Location Services** → Extract GPS or manual selection → Validate coordinates
4. **Automation** → Playwright navigates portal → Files complaint automatically
5. **Human Verification** → User solves CAPTCHA → Completes submission

### **Complete Project Structure**
```
StreetVision/ (Root Directory)
├── 📁 backend/                    # FastAPI Backend Server
│   ├── main.py                   # Core API endpoints & business logic
│   ├── requirements.txt          # Python dependencies
│   ├── Procfile                  # Deployment configuration
│   ├── render.yaml              # Render.com deployment config
│   ├── README.md                # Backend documentation
│   └── uploads/                 # Temporary image storage
│
├── 📁 frontend/                   # Web User Interface
│   ├── index.html               # Complete responsive UI
│   └── README.md                # Frontend deployment guide
│
├── 📁 Playwright/                 # Browser Automation
│   ├── codegen_complain.py      # Main automation script
│   └── location/                # GPS & location services
│       └── track.py             # EXIF GPS extraction & maps
│
├── 📁 Notebooks/                  # Data Science & Analysis
│   ├── model_analysis_visualization.ipynb  # Model performance analysis
│   └── road.ipynb               # Dataset exploration & training
│
├── 📁 deployment_models/          # AI Models (Ready for Production)
│   ├── Custom CNN Models        # 94% accuracy lightweight models
│   ├── VGG Models               # 96% accuracy trusted models
│   └── Model Artifacts          # Weights, architecture, metadata
│
├── 📁 pothole_dataset/           # Training Dataset
│   ├── normal/                  # Clean road images
│   └── potholes/               # Pothole images
│
└── 📄 README.md                  # This comprehensive project overview
```

---

## 📸 User Flow

1. **Image Analysis**: Upload pothole photo → AI detection
2. **Report Details**: Enter mobile, password, location
3. **Submit Complaint**: Agentic automation files official complaint (human solves CAPTCHA)
4. **Confirmation**: User receives status and PDF report

---

## 💡 Project Relevance

- **Solves a real-world problem**: Streamlines road complaint filing for citizens
- **Agentic design**: Combines automation with human oversight for reliability
- **End-to-end solution**: From image upload to government submission
- **Scalable architecture**: Ready for multi-domain expansion (roads, utilities, environment)

---

## 🔮 Future Scope

- **OAuth 2.0 Authentication**: Secure user login and multi-provider support
- **Multi-domain Detection**: Expand to cracks, traffic signs, waste management, etc.
- **Mobile App**: Real-time reporting from smartphones
- **Advanced AI**: Multi-modal models (vision, language, audio)
- **Global Scaling**: Multi-language support, international government APIs
- **Smart City Integration**: IoT sensors, edge computing, predictive analytics

---

## 📦 Complete Project

StreetVision is a fully integrated, production-ready platform combining:

### **🎯 Core Components**
- **🚀 FastAPI Backend** (backend/) - High-performance async API with TensorFlow integration
- **🎨 Modern Frontend** (frontend/) - Responsive HTML/CSS/JS interface deployed on Netlify
- **🤖 Playwright Automation** (Playwright/) - Intelligent browser automation with human-in-loop
- **📊 Jupyter Notebooks** (Notebooks/) - Data science workflow and model analysis
- **🧠 AI Models** (deployment_models/) - Custom CNN & VGG models ready for production
- **📸 Dataset Management** (pothole_dataset/) - Curated training data for model development

### **🔧 Development Workflow**
1. **Data Science** → Notebooks for experimentation and model training
2. **Backend Development** → FastAPI with TensorFlow model integration
3. **Frontend Development** → Modern responsive UI with real-time feedback
4. **Automation Development** → Playwright scripts for government portal interaction
5. **Deployment** → Frontend on Netlify, backend ready for cloud deployment

### **🏗️ Production Ready Features**
- **Scalable Architecture** → Microservices design with clear separation of concerns
- **Robust Error Handling** → Comprehensive validation and graceful degradation
- **Security Implementation** → Input sanitization, file validation, and secure API design
- **Performance Optimization** → Async operations, efficient model loading, and caching
- **Documentation** → Complete README files for each component
- **Testing Ready** → Structured codebase ready for unit and integration testing

---

## 📚 Contributing & License

### **🤝 Contributing**
We welcome contributions to StreetVision! Here's how you can help:

1. **Fork the repository** on GitHub
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### **📋 Areas for Contribution**
- **AI Model Improvements** → Enhance detection accuracy or add new road defect types
- **Frontend Features** → Improve UI/UX, add new interactive components
- **Automation Enhancements** → Extend to other government portals or regions
- **Documentation** → Improve guides, add tutorials, or translate content
- **Testing** → Add unit tests, integration tests, or performance benchmarks

### **📄 License**
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**MIT License Summary:**
- ✅ **Commercial use** allowed
- ✅ **Modification** allowed  
- ✅ **Distribution** allowed
- ✅ **Private use** allowed
- ❗ **License and copyright notice** required
- ❌ **No warranty** provided

---

## 📞 Contact & Support

- **Author**: Mayank Dew ([GitHub](https://github.com/MayankDew08))
- **Project**: [StreetVision](https://github.com/MayankDew08/streetvision)

---

## 👨‍💼 About the Author

**Mayank Dew**  
*Full-Stack AI Engineer & Machine Learning Enthusiast*

🎓 **Expertise:** Deep Learning, Computer Vision, Web Development, Browser Automation  
🚀 **Specializes in:** End-to-end AI solutions, from research to production deployment  
💼 **Focus Areas:** Real-world problem solving with cutting-edge technology

### **📧 Professional Contact**
- **Email:** [mayank24102@iiitnr.edu.in](mailto:mayank24102@iiitnr.edu.in)
- **LinkedIn:** [Connect with me](https://www.linkedin.com/in/mayank-dewangan-913720321/)
- **GitHub:** [@MayankDew08](https://github.com/MayankDew08)

### **🤝 Collaboration & Opportunities**
- **Open to:** Full-time opportunities, consulting projects, and collaborative research
- **Available for:** Technical discussions, code reviews, and mentoring
- **Interested in:** AI/ML projects, startup collaborations, and open-source contributions

*Feel free to reach out for technical discussions, collaboration opportunities, or if you've successfully deployed this project with newer TensorFlow versions!*

---

## 🏁 Final Note

StreetVision demonstrates the power of combining deep learning, agentic automation, and beautiful frontend engineering to solve real-world problems. This **complete end-to-end project** showcases:

### **💼 Professional Development Skills**
- **Full-Stack Development** → Frontend, Backend, Database, and Deployment
- **Machine Learning Engineering** → Model training, evaluation, and production deployment
- **DevOps & Automation** → Browser automation, CI/CD ready, and cloud deployment
- **Data Science Workflow** → From data collection to model analysis and visualization
- **Software Architecture** → Microservices, API design, and scalable system architecture

### **🎓 Technical Mastery Demonstrated**
- **10+ Technologies** integrated seamlessly across the stack
- **Production-Ready Code** with proper error handling and validation
- **Documentation Excellence** with comprehensive README files for each component
- **Real-World Problem Solving** addressing actual citizen and government needs
- **Innovation in AI** combining custom models with trusted pre-trained solutions

### **🚀 Industry-Ready Project**
- **Deployable Solution** with frontend live on Netlify and backend cloud-ready
- **Scalable Architecture** designed for growth and feature expansion
- **Professional Standards** following best practices in coding, documentation, and deployment
- **Portfolio Showcase** demonstrating full-stack AI engineering capabilities

*Making roads safer, one intelligent complaint at a time.*

---

**🔗 Repository Structure Complete** | **📱 Live Demo Ready** | **🌟 Production Deployed**
