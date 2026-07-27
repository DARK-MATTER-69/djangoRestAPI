import requests

endpoint = "http://localhost:8000/api"

data = {
    'name':"mangue",
    'price':1100,
    'description':"fruit"
}

response = requests.post(endpoint, json=data)
print(response.json())
print(response.status_code) 