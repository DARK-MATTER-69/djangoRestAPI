import requests

endpoint = "http://localhost:8000/api/produit/"

data = {
    'name':"Orange",
    'price':1100,
    'description':"fruit",
}

response = requests.get(endpoint, json=data)
print(response.json())
print(response.status_code) 