# FELIPE BARROS DE GOUVEIA TOME RM568371

import socket as s, sys

ALVO = '10.3.40.100'
PORTA = 5000

try:
    con = s.socket(s.AF_INET,s.SOCK_STREAM)
    con.settimeout(10)
    con.connect((ALVO,PORTA))

    resp = con.recv(4096)

    # con.sendall(().encode())    
        
    #recuperando a mensagem enviada
    print("Resposta:", resp.decode(errors="ignore").rstrip(), flush=True)
    resp_split = resp.decode(errors="ignore").split(': ')

    pergunta = resp_split[1].split(' e ')
    # print(pergunta)

    soma = str(int(pergunta[0]) + int(pergunta[1]))
    print(f'Soma dos números: {soma}')

    con.send(soma.encode())
    print(con.recv(4096))

    con.close()
except Exception as e:
    print(e)