# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = float(input('Digite um número decimal: '))

result1 = (num1 * 2) * (num2 / 2)
print('O produto do dobro do primeiro com metade do segundo: ',result1)

result2 = (num1 * 3) + num3
print('A soma do triplo do primeiro com o terceiro: ',result2)

result3 = num3 ** 3
print('O terceiro elevado ao cubo: %.2f'%result3)
