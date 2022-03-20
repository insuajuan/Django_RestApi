import requests

endpoint = "http://localhost:8000/api/"

resp = requests.post(endpoint, json={"title": "Hello World"})
print(resp.text)
print(resp.status_code)