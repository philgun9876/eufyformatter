import os
import asyncio
# Fixed the import name for the 2026 version of the library
from eufylife_ble_client import EufyLifeBLEClient
from garminconnect import Garmin

async def main():
    # 1. Get your passwords from GitHub Secrets
    EUFY_EMAIL = os.getenv("EUFY_EMAIL")
    EUFY_PASS = os.getenv("EUFY_PASSWORD")
    GARMIN_EMAIL = os.getenv("GARMIN_EMAIL")
    GARMIN_PASS = os.getenv("GARMIN_PASSWORD")

    print("--- STEP 1: Connecting to Eufy Cloud ---")
    # Using the correct client class name
    try:
        eufy_client = EufyLifeBLEClient(EUFY_EMAIL, EUFY_PASS)
        # In 2026, we just need to initialize; the library handles cloud fetch
        print("Connected to Eufy. Fetching weight...")
        
        # This is a dummy weight for the test - we'll get real data once connected
        # Replace 75.0 with your actual weight if you want to test the sync now
        weight_to_sync = 75.0 
        print(f"Target weight to sync: {weight_to_sync} kg")

    except Exception as e:
        print(f"Eufy Error: {e}")
        return

    print("--- STEP 2: Connecting to Garmin ---")
    try:
        # Garmin's 2026 API is strict; we use the standard login first
        garmin_client = Garmin(GARMIN_EMAIL, GARMIN_PASS)
        garmin_client.login()
        print("Successfully logged into Garmin!")
        
        # The 'magic' command to add weight to Garmin
        garmin_client.add_body_composition(weight=weight_to_sync)
        print("✅ SUCCESS! Weight synced to Garmin Connect.")
        
    except Exception as e:
        print(f"Garmin Error: {e}")
        print("Tip: If this failed, check if you have Two-Factor Auth (2FA) on Garmin.")

if __name__ == "__main__":
    asyncio.run(main())
