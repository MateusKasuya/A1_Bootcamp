# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano

data = input('Insira uma data no formato dd/mm/aaaa: ')

separador = '/'

split_data = data.split(separador)

print(f'Dia: {split_data[0]}')
print(f'Mês: {split_data[1]}')
print(f'Ano: {split_data[2]}')