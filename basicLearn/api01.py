import requests

r = requests.get("http://39.107.96.138:3000/api/v1/topics")
# print(r,type(r))
# print(r.json())
data = r.json()
print(data["success"])