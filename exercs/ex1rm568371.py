import string
import random

caracteres = int(input('Escolha quantos caracteres para a senha: '))
alfabeto = string.ascii_letters + string.digits + string.punctuation
password = ''
for i in range(caracteres):
    if i < caracteres:
        password += random.choice(alfabeto)
    else:
        break
print(password)