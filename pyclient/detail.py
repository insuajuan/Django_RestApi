import requests


endpoint = "http://localhost:8000/api/products/5/"


get_resp = requests.get(endpoint)

print(get_resp.json())