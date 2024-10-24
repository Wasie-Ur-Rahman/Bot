import requests

# BASE_API_URL = "http://0.0.0.0:8000"
BASE_API_URL = "https://t5dpw1tm-8000.inc1.devtunnels.ms/docs"
def signup(username, email, password):
    response = requests.post(
        f"{BASE_API_URL}/signup/",
        json={"username": username, "email": email, "password": password}
    )
    return response

def login(username, password):
    response = requests.post(
        f"{BASE_API_URL}/login/",
        json={"username": username, "password": password}
    )
    return response

def validate_url(url):
    response = requests.post(f"{BASE_API_URL}/validate-url/", json={"url": url})
    return response

def extract_data():
    response = requests.post(f"{BASE_API_URL}/extract-data/")
    return response


def report():
    response = requests.post(f"{BASE_API_URL}/Report/")
    return response