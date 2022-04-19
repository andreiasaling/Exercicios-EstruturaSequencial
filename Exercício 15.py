# 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo

salario_hora = float(input('Valor recebido por hora: '))
horas_trabalhadas = float(input('Quantidade de horas trabalhadas: '))
salario_bruto = salario_hora * horas_trabalhadas
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)


print(f'+ Salário Bruto: R$ {salario_bruto}')
print(f'- IR (11%): R$ {imposto_renda}')
print(f'- INSS (8%): R$ {inss}')
print(f'- Sindicato (5%): R$ {sindicato}')
print(f'= Salário Líquido: R$ {salario_liquido}')

