import requests
import time

# Configuration
URL = "http://your-application-url"  # Replace with the application's URL
CHECK_INTERVAL = 60  # Time in seconds between checks
UP_STATUS_CODES = {200, 201, 202}  # HTTP status codes considered as 'up'

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code in UP_STATUS_CODES:
            return "UP"
        else:
            return "DOWN"
    except requests.RequestException:
        return "DOWN"

def monitor_application():
    while True:
        status = check_application_status(URL)
        print(f"Application Status: {status}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    print("Starting application health checker...")
    monitor_application()
