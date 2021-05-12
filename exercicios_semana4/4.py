''' Escreva um programa que solicita que o usuário digite dois números
quaisquer e um operador matemático. A partir das informações,
realizar a operação desejada. '''

x = float(input('Digite o primeiro valor: '))
y = float(input('Digite o segundo valor: '))
print('Faça algumas das seguintes operações: \nSoma(+) \nSubtração(-) \nMultiplicação(*) \nDivisão(/)')
escolha = input('Escolha uma operação matemática utilizando o seu simbolo: ')
if escolha == '+':
    print(f'A Soma é: {x + y}')
elif escolha == '-':
    print(f'A Subtração é: {x - y}')
elif escolha == '*':
        print(f'A Multiplicação é: {x * y}')
elif escolha == '+':
    print(f'A Divisão é: {x / y}')
else:
    print('Operador INVÁLIDO digite novamente:')




