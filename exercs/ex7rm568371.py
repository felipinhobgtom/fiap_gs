while True:
    numeros = input('Digite três números separados por espaço: ')
    lista_numeros = numeros.split(' ')

    print(f'Maior: {max(lista_numeros)}')
    print(f'Menor: {min(lista_numeros)}')
    print(f'Soma de todos: {int(lista_numeros[0]) + int(lista_numeros[1]) + int(lista_numeros[2])}')