# 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
# sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

area_pintar = float(input('Qual o tamanho (em m²) da área a ser pintada? '))
litros_tinta = area_pintar / 6
print('\nSerá utilizado %.2f litros de tinta'%litros_tinta)

qtde_latas_tinta = litros_tinta / 18
qtde_galoes_tinta = litros_tinta / 3.6
print(f'Serão necessárias {qtde_latas_tinta} latas de tinta.')
print(f'Serão necessárias {qtde_galoes_tinta} galões de tinta.')

valor_latas = math.ceil(qtde_latas_tinta) * 80
valor_galoes = math.ceil(qtde_galoes_tinta) * 25
print(f'\nValor total em Latas de 18 litros: R$ %.2f'%valor_latas)
print(f'Valor total em Galões de 3,6 litros: R$ %.2f'%valor_galoes)


print('\nConsiderando o menor desperdício de tinta, temos: \n')

qtd_latas_mistas18 = ((litros_tinta * 0.10) + litros_tinta) / 18
qtd_litros18 = math.trunc(qtd_latas_mistas18) * 18
resto18 = ((litros_tinta * 0.10) + litros_tinta) - qtd_litros18
qtd_latas_mistas36 = resto18 / 3.6
qtd_latas_mistas_total = math.trunc(qtd_latas_mistas18) + math.ceil(qtd_latas_mistas36)
valor_misto18 = math.trunc(qtd_latas_mistas18) * 80
valor_misto36 = math.ceil(qtd_latas_mistas36) * 25
total_misto = valor_misto18 + valor_misto36

print('Quantidade de latas de 18 litros: {}'.format(math.trunc(qtd_latas_mistas18)))
print('Quantidade de galões de 3,6 litros: {}'.format(math.ceil(qtd_latas_mistas36)))
print('Quantidade latas/galões mistas: {}'.format(qtd_latas_mistas_total))
print('\nO valor total considerando GALÕES e LATAS é (acresentando 10% de quebra): R$ {}'.format(total_misto))