# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperatura_celcius = float(input('Temperatura em °C: '))
temperatura_fahreheit = (1.8 * temperatura_celcius)+32

print('A Temperatura convertida é de %.1f °F'%temperatura_fahreheit)

