import requests

res = requests.get("http://127.0.0.1:5000/api/flights/2")
res.json()
print(res.json())
print(res.json()['passengers'])

res2 = requests.get("http://127.0.0.1:5000/api/flights/200")
res2.json()
print(res2.json())
print(res2.status_code)