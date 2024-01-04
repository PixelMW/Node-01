import requests
import time

def ping_google():
    try:
        response = requests.get('http://www.google.com', timeout=5)
        # Check the status code to ensure a successful request
        if response.status_code == 200:
            print("Ping successful")
        else:
            print(f"Ping failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")

def keep_system_active(interval_seconds):
    while True:
        ping_google()
        time.sleep(interval_seconds)

if __name__ == "__main__":
    # Set the interval (in seconds) at which you want to ping Google
    ping_interval = 3  # 3 seconds
    
    keep_system_active(ping_interval)
