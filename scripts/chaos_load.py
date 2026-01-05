import requests
import time
import random


endpoints = ["/", "/heavy", "/error", "/heavy"] #weighted towards /heavy
print("Starting chaos load generator... Press Ctrl+C to stop.")

while True:
    target = random.choices(endpoints)
    try:
        url = f"http://localhost:8000{target}"
        resp = requests.get(url)
        print(f"Hit {url} - Status Code: {resp.status_code}")
    except Exception as e:
        print(f"Connection error {url}: {e}")
    
    #random interval between requests, to simulate real users:
    time.sleep(random.uniform(0.1, 1.0))