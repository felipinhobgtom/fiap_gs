import os

nova_pasta = input('Digite o nome da nova pasta: ')
os.mkdir(nova_pasta)
print(f'Pasta criada (ou já existente) {nova_pasta}')

novo_arquivo = input('Digite o nome do arquivo (sem extensão): ')
with open(f'{nova_pasta}/{novo_arquivo}.txt', 'w') as f:
    content = input('Digite o conteúdo do arquivo: ')
    f.write(content)
print(f'Arquivo criado com sucesso em: {nova_pasta}/{novo_arquivo}.txt')