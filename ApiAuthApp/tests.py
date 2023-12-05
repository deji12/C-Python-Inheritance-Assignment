from django.test import TestCase

# Create your tests here.
import requests

token = "895bc4829a720ee314d966397a8d8edc6777e7ef"

request = requests.post(
    "http://127.0.0.1:8000/course/create-course/",
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
)

print(request.json())