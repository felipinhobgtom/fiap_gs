# FELIPE BARROS DE GOUVEIA TOME RM568371

import requests

id = 4
API_4 = f"https://jsonplaceholder.typicode.com/users/{id}"
res = requests.get(API_4)

payload = res.json()

print(f'Nome: {payload['name']}')
print(f'E-mail: {payload['email']}')

res_posts = requests.get('https://jsonplaceholder.typicode.com/posts')
posts_payload = res_posts.json()

for post in posts_payload:
    if post['userId'] == id:
        print(f'Titulo: {post['title']}')