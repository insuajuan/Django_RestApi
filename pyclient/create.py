import requests


endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "this field is done",
    "price": 12.98
}

post_resp = requests.post(endpoint, json=data)

print(post_resp.json())