# 1) Solicita ao usuario que digite seu nome

nome = input('Digite o seu nome: ')

# 2) Solicita ao usuário que digite o valor do seu salário
salario = float(input('Insira o seu salário: '))

# 3) Solicita ao usuário que digite o valor do bônus recebido

bonus = float(input('Qual foi o seu bônus? '))

# 4) Calcule o valor do bônus final (1000 + salario * bonus)

CONSTANTE_BONUS = 1000
bonus_final = CONSTANTE_BONUS + salario * bonus

# 5) Imprima a mensagem personalizada incluindo o nome do usuario e o bônus final

print(f'O usuario {nome} possui o bônus de {bonus_final}')