import requests

# URL
url = 'http://localhost:5000/api/'

# Change the value of pieces that you want to test
payload = {
	'exp':0.0
}

r = requests.post(url,json=payload)

print(r.json())
