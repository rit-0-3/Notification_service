import requests

url = 'http://127.0.0.1:5000/notifications'
headers = {'Content-Type': 'application/json'}
data = {
    "user_id": 1,
    "type": "email",
    "message": "Hello from Rit!"
}

response = requests.post(url, json=data, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.json())
