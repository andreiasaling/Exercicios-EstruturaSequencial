''' 18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

tamanho_arquivo = float(input('Qual o tamanho do arquivo para download (em MB)? '))
velociade_internet = float(input('Qual a velocidade da internet (em Mbps)? '))

tempo_download = (tamanho_arquivo / (velociade_internet/8)) / 60

print('O tempo aproximado de download é de %.1f minutos.'%tempo_download)
