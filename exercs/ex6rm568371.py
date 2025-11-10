# FELIPE BARROS DE GOUVEIA TOME RM568371

import requests

API_3 = "https://httpbin.org/get"
res = requests.get(API_3, headers={
    'User-Agent': 'nao'
})

payload = res.json()
headers = payload['headers']

print(f'Headers: {headers}')
print(f'User agent: {headers['User-Agent']}')
print(f'Status code: {res.status_code}')