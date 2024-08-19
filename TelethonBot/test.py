import httpx

response = httpx.post('https://my.telegram.org/auth/send_password' , params={"phone" : "+998935336533"})
print(response.status_code)
response_hash = response.json().get('random_hash')
print()
password = input('Password >>>')
response = httpx.post('https://my.telegram.org/auth/login' , params={"password" : password , 'random_hash' : response_hash})
print(response)


