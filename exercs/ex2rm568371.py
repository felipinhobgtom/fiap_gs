# FELIPE BARROS DE GOUVEIA TOME RM568371

import os

while True:
    site = input("Digite um site: ")
    ping = os.popen(f"ping {site} -n 1")
    
    # isso aq ta uma gambiarra nojenta jesus
    ponga = str(ping.read()).split(' ')
    # print(ponga)
    
    if ponga[0] == '\nPinging':
        ip_string = ponga[12].split('\n')[0]
        ttl_string = ponga[9].split(':')[0]
        print(f"Host respondeu! IP: {ip_string}, TTL: {ttl_string}")
    else:
        print('Host não respondeu.')