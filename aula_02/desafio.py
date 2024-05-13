# Faça um programa que você insira o seu nome e faça validações de erro

nome = input('Digite o seu nome: ')

if nome.isdigit():
    print('Digitou seu nome errado')
    exit()
elif len(nome) == 0:
    print('Você não digitou nada')
    exit()
elif nome.isspace():
    print('Você digitou somente espaço')
    exit()
else:
    print(f'Seu nome é {nome}')
