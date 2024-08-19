import requests
url = "https://open.er-api.com/v6/latest"
response = requests.get(url)
money = response.json().get('rates').get('UZS')
print(float(money))