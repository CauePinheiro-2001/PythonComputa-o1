'''2.Faça um programa que receba dois números inteiros e gere os
números inteiros que estão  no intervalo compreendido por eles.
O segundo número deve, necessariamente, ser maior do que o primeiro'''

#As variáveis
valor1 = int(input('Digite o Primeiro número: '))
valor2 = int(input('Digite o Segundo número (maior que o primeiro): '))

#Caso o segundo valor fosse menor que o primeiro, deve atribuir o segundo valor novamente
while valor2 < valor1:
    print('Valor inválido, escreva novamente')
    valor2 = int(input('Digite o segundo numero novamente, maior que o primeiro: '))
print('Os números inteiros que estão no intervalo entre eles são:')

#Mostrar os valores entre valor1 e valor2:
while valor1 < valor2 - 1:
    valor1 = valor1 + 1
    print(valor1)