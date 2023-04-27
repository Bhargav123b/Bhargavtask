import requests

url = 'http://127.0.0.1:5000/v1/sanitized/input/'

# Test case 1 - Sanitized input
data = {'payload': 'Bhargav'}
response = requests.post(url, json=data)
print(response.json())   # expected output: {"result": "sanitized"}
assert response.json() == {'result': 'sanitized'}

# Test case 2 - Unsanitized input
data = {'payload': 'Bhargav;'}
response = requests.post(url, json=data)
print(response.json())   # expected output: {"result": "unsanitized"}
assert response.json() == {'result': 'unsanitized'}