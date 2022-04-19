# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input('Valor recebido por hora: '))
horas_trabalhadas = float(input('Quantidade de horas trabalhadas: '))
salario = salario_hora * horas_trabalhadas
print('Salário: R$ ',salario)