import requests

endpoint = "http://localhost:8000/api/product/1/"

# data = {
#     'name':"Orange",
#     'price':1100,
#     'description':"fruit",
# }

response = requests.post(endpoint)
print(response.json())
print(response.status_code) 