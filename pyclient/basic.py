import requests

endpoint = "http://localhost:8000/"

resp = requests.get(endpoint, json={"query": "Hello World"})
print(resp.text)
print(resp.status_code)