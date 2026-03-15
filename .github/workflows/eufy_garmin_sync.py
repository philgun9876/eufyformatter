import os
from eufylife_ble_client import EufyLifeClient
from garminconnect import Garmin

# Load your secrets from GitHub
eufy_email = os.getenv("EUFY_EMAIL")
eufy_password = os.getenv("EUFY_PASSWORD")
garmin_email = os.getenv("GARMIN_EMAIL")
garmin_password = os.getenv("GARMIN_PASSWORD")

def main():
    print("Connecting to Eufy...")
    # Logic to fetch latest weight from Eufy Cloud
    # and push to Garmin Connect using the 'garth' library
    try:
        client = Garmin(garmin_email, garmin_password)
        client.login()
        print("Successfully logged into Garmin!")
        # Trigger the weight upload here
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    main()
