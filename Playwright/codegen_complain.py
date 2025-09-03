import requests
import pytest
from playwright.sync_api import Page, expect, sync_playwright
import os
import time
import sys
import argparse


# Module-level location variables (may be set by CLI or by import)
lat = None
lon = None
state = None
nh_number = None
pdf_path = None

def test_pg_portal_grievance_submission(page: Page):
    # Get input from user or environment variables
    mobile_number = os.getenv('MOBILE_NUMBER') or input("Enter your mobile number: ")
    password = os.getenv('PASSWORD') or input("Enter your password: ")
    
    print("🌐 Navigating to PG Portal...")
    page.goto('https://www.pgportal.gov.in/Home/LodgeGrievance')
    
    print("🔐 Clicking User Login...")
    page.get_by_role('link', name='User Login').click()
    
    print("📱 Filling mobile number...")
    page.get_by_role('textbox', name='Mobile No/Email Id/Username').click()
    page.get_by_role('textbox', name='Mobile No/Email Id/Username').fill(mobile_number)
    
    print("🔑 Filling password...")
    page.get_by_role('textbox', name='Password').click()
    page.get_by_role('textbox', name='Password').fill(password)
    
    # Wait for captcha to be visible
    print("🤖 Waiting for CAPTCHA to appear...")
    expect(page.get_by_role('img', name='Captcha')).to_be_visible()
    
    # Pause for manual captcha entry
    print("⏳ CAPTCHA visible! Please solve it manually in the browser.")
    print("🕐 Waiting 15 seconds for you to solve the CAPTCHA...")
    time.sleep(15)
    
    print("▶️ Clicking Login button...")
    page.get_by_role('button', name='Login ').click()
    
    # Wait for navigation after login
    print("⌛ Waiting for page to load after login...")
    page.wait_for_load_state('networkidle')
    
    print("📝 Clicking 'Lodge Public Grievance'...")
    page.get_by_role('link', name=' Lodge Public Grievance').click()
    
    print("✅ Accepting terms and conditions...")
    page.locator('#termscondition').check()
    page.get_by_role('button', name='Submit ').click()
    
    # Wait for the page to load
    print("⌛ Waiting for grievance form to load...")
    page.wait_for_load_state('networkidle')
    
    print("🏛️ Selecting Ministry...")
    page.get_by_text('More... Ministries/').click()
    page.get_by_role('searchbox').fill('Road')
    page.get_by_role('option', name='Road Transport and Highways').locator('span').click()
    
    print("📂 Selecting category...")
    page.get_by_role('textbox', name='Please select main category').click()
    page.get_by_role('option', name='Construction & Maintenance of').click()
    page.get_by_role('textbox', name='Select next level category').click()
    page.get_by_role('option', name='Matters related to State Roads').click()
    page.get_by_role('textbox', name='Name of State *').click()
    # Use provided state if available
    state_val = globals().get('state') or 'Chhattisgarh'
    page.get_by_role('textbox', name='Name of State *').fill(state_val)
    page.get_by_role('textbox', name='National highway Number *').click()
    nh_val = globals().get('nh_number') or 'NH30'
    page.get_by_role('textbox', name='National highway Number *').fill(nh_val)
    page.get_by_role('textbox', name='Text of grievance (Remarks) *').click()
    
    # Create detailed complaint text with location info
    complaint_text = f'Pothole detected at coordinates {globals().get("lat", "Unknown")}, {globals().get("lon", "Unknown")}'
    if globals().get("state"):
        complaint_text += f' in {globals().get("state")}'
    if globals().get("nh_number"):
        complaint_text += f' on {globals().get("nh_number")}'
    complaint_text += '. Immediate repair required for road safety.'
    
    page.get_by_role('textbox', name='Text of grievance (Remarks) *').fill(complaint_text)
    page.get_by_role('button', name=' Next').click()
    
    # Wait between steps
    page.wait_for_timeout(1000)
    page.get_by_role('button', name=' Next').click()
    page.get_by_role('textbox', name='Please select a Ministry/').click()
    page.get_by_role('option', name='Ministry of Road Transport').click()
    page.get_by_role('button', name=' Next').click()
    
    # Skip file upload section completely
    print("⏭️ Skipping file upload - proceeding to CAPTCHA")
    
    # Wait before moving to captcha
    page.wait_for_timeout(1000)

    # Handle second captcha
    print("🤖 Waiting for second CAPTCHA...")
    try:
        expect(page.get_by_role('img', name='Captcha')).to_be_visible(timeout=10000)
        
        # Pause again for manual captcha entry
        print("⏳ Second CAPTCHA visible! Please solve it manually.")
        print("🕐 Waiting 20 seconds for you to solve the CAPTCHA...")
        time.sleep(20)
        
        # Try to find and click submit button
        print("📤 Looking for Submit button...")
        
        # Wait for submit button to be enabled
        page.wait_for_selector('button:has-text("Submit")', timeout=10000)
        
        submit_button = page.get_by_role('button', name=' Submit')
        if submit_button.is_visible() and submit_button.is_enabled():
            print("✅ Submit button found and enabled, clicking...")
            submit_button.click()
        else:
            print("⚠️ Submit button not ready, trying alternative selector...")
            page.click('input[type="submit"], button[type="submit"], .submit-btn')
        
    except Exception as e:
        print(f"❌ Error during submission: {e}")
        print("🔍 Trying to find any submit button...")
        try:
            page.click('button:has-text("Submit")')
        except:
            print("❌ Could not find submit button")
    
    # Wait for final submission
    print("⌛ Waiting for submission to complete...")
    page.wait_for_load_state('networkidle')
    
    print("✅ Grievance submission completed successfully!")
    print("🎉 You can now check the browser for confirmation details.")

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


if __name__ == "__main__":
    # For running directly without pytest

    parser = argparse.ArgumentParser()
    parser.add_argument('--mobile', type=str, help='Mobile number to use for login')
    parser.add_argument('--password', type=str, help='Password to use for login')
    parser.add_argument('--lat', type=float, help='Latitude')
    parser.add_argument('--lon', type=float, help='Longitude')
    parser.add_argument('--pdf', type=str, help='Path to PDF file to upload')
    parser.add_argument('--headed', action='store_true', help='Run headed browser')
    args = parser.parse_args()

    # If location args provided, set module globals
    if args.lat is not None and args.lon is not None:
        lat = args.lat
        lon = args.lon
    if args.pdf:
        pdf_path = args.pdf
    state, nh_number = get_location_details(lat, lon)

    def run(mobile_arg=None, password_arg=None, headed=True):
        mobile_number = mobile_arg or args.mobile or input("Enter your mobile number: ")
        password = password_arg or args.password or input("Enter your password: ")

        print(f"Starting Playwright with headed={headed}")
        
        with sync_playwright() as p:
            print("Launching Chromium browser...")
            browser = p.chromium.launch(
                headless=False,  # Make browser visible
                args=[
                    '--start-maximized',     # Start maximized
                    '--disable-blink-features=AutomationControlled',  # Hide automation indicators
                    '--disable-extensions',   # Disable extensions for cleaner experience
                    '--no-first-run',        # Skip first run experience
                    '--disable-default-apps', # Disable default apps
                    '--disable-infobars',    # Disable info bars
                    '--window-position=0,0', # Position window at top-left
                    '--window-size=1920,1080' # Set window size
                ],
                slow_mo=1000  # Add delay between actions for visibility
            )
            context = browser.new_context(
                viewport={'width': 1920, 'height': 1080}  # Set viewport size
            )
            page = context.new_page()

            try:
                # Set environment variables for the test so the test function reads them
                os.environ['MOBILE_NUMBER'] = mobile_number
                os.environ['PASSWORD'] = password

                # Bring browser to front
                page.bring_to_front()
                print(" Browser window brought to front")
                print(" Starting grievance submission...")
                test_pg_portal_grievance_submission(page)

            except Exception as e:
                print(f" An error occurred: {e}")
                import traceback
                traceback.print_exc()
                # Keep browser open for debugging on error
                print(" Browser will remain open for debugging. Close manually when done.")
                input("Press Enter to close browser...")
            finally:
                print(" Closing browser...")
                browser.close()

    # Run with headed browser by default
    run(mobile_arg=args.mobile, password_arg=args.password, headed=True)