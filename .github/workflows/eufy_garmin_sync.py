import os
import requests
from garminconnect import Garmin

def get_eufy_weight(email, password):
    print("Connecting to Eufy Cloud...")
    # This is the direct 2026 Eufy API endpoint for scale data
    login_url = "https://mysecurity.eufylife.com/api/v1/passport/login"
    payload = {"email": email, "password": password, "type": 1}
    
    try:
        # 1. Login to Eufy
        response = requests.post(login_url, json=payload).json()
        token = response['data']['auth_token']
        
        # 2. Get latest weight entry
        data_url = "https://mysecurity.eufylife.com/api/v1/app/device/last_device_data"
        headers = {"X-Auth-Token": token}
        weight_data = requests.get(data_url, headers=headers).json()
        
        # Extract weight (usually in kg)
        weight = float(weight_data['data']['weight']) / 100 # Converting from grams if needed
        return weight
    except Exception as e:
        print(f"Eufy Fetch Failed: {e}")
        return None

def main():
    eufy_user = os.getenv("EUFY_EMAIL")
    eufy_pass = os.getenv("EUFY_PASSWORD")
    garmin_user = os.getenv("GARMIN_EMAIL")
    garmin_pass = os.getenv("GARMIN_PASSWORD")

    weight = get_eufy_weight(eufy_user, eufy_pass)
    
    if weight:
        print(f"Found weight: {weight} kg. Syncing to Garmin...")
        try:
            client = Garmin(garmin_user, garmin_pass)
            client.login()
            client.add_body_composition(weight=weight)
            print("✅ SUCCESS! Check your Garmin app.")
        except Exception as e:
            print(f"Garmin Error: {e}")

if __name__ == "__main__":
    main()
