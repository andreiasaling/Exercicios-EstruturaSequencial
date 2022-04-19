# 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
# ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area_pintar = float(input('Qual o tamanho (em m²) da área a ser pintada? '))
litros_tinta = area_pintar / 3
latas_tinta = litros_tinta / 18
valor = latas_tinta * 80

print(f'Serão necessárias {latas_tinta} latas de tinta.\nO valor total é de R$ {valor}')