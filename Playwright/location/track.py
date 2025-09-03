from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import requests
import webbrowser
import json
import argparse

# ---------- EXIF Functions ----------
def get_exif_data(image):
    exif_data = {}
    try:
        img = Image.open(image)
        info = img._getexif()
        if info:
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                if decoded == "GPSInfo":
                    gps_data = {}
                    for t in value:
                        sub_decoded = GPSTAGS.get(t, t)
                        gps_data[sub_decoded] = value[t]
                    exif_data[decoded] = gps_data
                else:
                    exif_data[decoded] = value
    except Exception as e:
        print(f"Error reading EXIF: {e}")
    return exif_data

def get_decimal_from_dms(dms, ref):
    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1]
    seconds = dms[2][0] / dms[2][1]
    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal

def get_lat_lon(exif_data):
    gps_info = exif_data.get("GPSInfo", {})
    if not gps_info:
        return None, None

    gps_lat = gps_info.get("GPSLatitude")
    gps_lat_ref = gps_info.get("GPSLatitudeRef")
    gps_lon = gps_info.get("GPSLongitude")
    gps_lon_ref = gps_info.get("GPSLongitudeRef")

    if gps_lat and gps_lat_ref and gps_lon and gps_lon_ref:
        lat = get_decimal_from_dms(gps_lat, gps_lat_ref)
        lon = get_decimal_from_dms(gps_lon, gps_lon_ref)
        return lat, lon
    return None, None

# ---------- Google Maps & Manual Coordinates ----------
def ask_for_manual_coordinates():
    print("\nOpening Google Maps for manual location selection...")
    print("Right-click on location → Copy coordinates → paste here.")
    webbrowser.open("https://www.google.com/maps")
    coords = input("Paste coordinates (format: lat,lon): ").strip()
    try:
        lat, lon = map(float, coords.split(","))
        return lat, lon
    except:
        print("Invalid format. Try again.")
        return ask_for_manual_coordinates()

# ---------- Reverse Geocoding ----------
def get_location_details(lat, lon):
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&zoom=18&addressdetails=1"
    headers = {'User-Agent': 'GeoExtractor/1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        address = data.get("address", {})
        state = address.get("state", "Unknown")
        road = address.get("road", "")
        highway = address.get("highway", "")
        
        nh_number = None
        if "NH" in road.upper() or "NATIONAL HIGHWAY" in road.upper():
            nh_number = road
        elif "NH" in highway.upper() or "NATIONAL HIGHWAY" in highway.upper():
            nh_number = highway
        
        return state, nh_number
    else:
        return "Unknown", None


def get_final_coordinates(image_path: str = "photo.jpg"):
    """Return final latitude and longitude for image_path.

    This encapsulates the interactive logic that used to run in __main__.
    It will try to read EXIF GPS first, and if not found will prompt the
    user to pick coordinates via Google Maps (interactive).
    """
    exif_data = get_exif_data(image_path)
    lat, lon = get_lat_lon(exif_data)

    if lat and lon:
        return lat, lon
    # Fallback to manual selection which will open Google Maps and ask user
    return ask_for_manual_coordinates()

# ---------- Main ----------
state, nh_number, lat, lon = None, None, None, None
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--mobile', type=str, help='Mobile number to use for login')
    parser.add_argument('--password', type=str, help='Password to use for login')
    parser.add_argument('--lat', type=float, help='Latitude')
    parser.add_argument('--lon', type=float, help='Longitude')
    args = parser.parse_args()


    print(f" Final coordinates: {args.lat}, {args.lon}")

    # Get state & highway info
    state, nh_number = get_location_details(args.lat, args.lon)
    print(f"State: {state}")
    print(f"National Highway: {nh_number if nh_number else 'Not on a national highway'}")
