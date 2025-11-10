# FELIPE BARROS DE GOUVEIA TOME RM568371

import requests, json

API_1 = 'https://api.ipify.org/'

response = requests.get(API_1)
meu_ip = response.text

API_2 = f'http://ip-api.com/json/{meu_ip}'

res = requests.get(API_2).json()
# print(res)

obj = {
    'Meu IP': meu_ip,
    'País': res['country'],
    'Cidade': res['regionName'],
    'Latitude/Longitude': f'{res['lat']}/{res['lon']}'
}

print(obj)