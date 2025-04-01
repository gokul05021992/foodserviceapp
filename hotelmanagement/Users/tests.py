from django.test import TestCase

# Create your tests here.
import requests
import concurrent.futures
import time

API_URL = "http://127.0.0.1:8000/api/send-otp/"  # Update with your actual API endpoint
TEST_EMAIL = "gokulpython123@gmail.com"

def send_otp_request(i):
    """ Function to send OTP request """
    payload = {"email":"malaboopathy1975@gmail.com"}  # Unique email per request
    headers = {"Content-Type": "application/json"}
    
    start_time = time.time()
    response = requests.post(API_URL, json=payload, headers=headers)
    end_time = time.time()

    print(f"Request {i}: Status {response.status_code}, Time Taken: {round(end_time - start_time, 4)} sec")
    return response.status_code

def run_load_test():
    """ Run 200 concurrent OTP requests """
    num_requests = 500

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(send_otp_request, i): i for i in range(num_requests)}
        
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  # Get results (if needed)
            except Exception as e:
                print(f"Request failed: {e}")

if __name__ == "__main__":
    start_time = time.time()
    run_load_test()
    total_time = round(time.time() - start_time, 2)
    print(f"Completed 500 requests in {total_time} seconds")
