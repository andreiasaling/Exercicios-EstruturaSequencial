# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# FÓRMULA: C = 5 * ((F-32) / 9)

temperatura_fahrenheit = float(input('Temperatura em °F: '))
temperatura_celcius = 5 * ((temperatura_fahrenheit-32) / 9)

print('A temperatura convertida é de %.1f °C'%temperatura_celcius)