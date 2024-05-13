# Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada

import math

raio = float(
    input(
        'Insira o raio do círculo: '
    )
)

area = math.pi * raio ** 2

print(area)