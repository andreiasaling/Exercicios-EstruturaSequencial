# 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input('Digite o raio do círculo: '))
area = math.pi*(raio*raio)
print('A área do círculo é %.2f'%(area))