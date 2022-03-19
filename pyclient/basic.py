import requests

endpoint = "http://localhost:8000/api/"

resp = requests.get(endpoint, params={"abc": 123}, json={"query": "Hello World"})
print(resp.text)
print(resp.status_code)