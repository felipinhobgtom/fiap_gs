with open('Linux.log', 'r', encoding='utf-8') as log:
    logs = []
    rhosts= []
    
    while True:
        linha = log.readline()
        
        if 'sshd' in linha:
            logs.append(linha)

            linha_split = linha.split('rhost=')
            # print(len(linha_split))

            if len(linha_split) > 1:
                rhost = linha_split[1]
                rhosts.append(rhost.split(' ')[0])

        if linha == '':
            break
    
    print(f'Quantidade total de acessos: {len(logs)}')
    print(f'Quantidade de hosts: {len(rhosts)}')
    print(f'Hosts que acessaram: {rhosts}')