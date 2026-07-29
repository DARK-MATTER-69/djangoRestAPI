import requests

endpoint = "http://localhost:8000/api/product/"

# data = {
#     "name":"Orange",
#     "price":1100,
#     "description":"fruit",
# }

response = requests.get(endpoint)
print(response.json())
print(response.status_code) 