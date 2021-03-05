'''8.Escreva   um   programa   que   lê   um   número inteiro.
Informe  se  o  mesmo  é  par  ou ímpar, positivo ou negativo.'''

print('Programa 8')
x = int(input('Informe um valor inteiro: '))
if (x % 2) == 0 and x >= 0:
    print("Numero Par e Positivo")
elif (x % 2) == 0 and x < 0:
    print('Numero Par e Negativo')
elif (x % 2) != 0 and x < 0:
    print('Numero Ímpar e Negativo')
else:
    print('Numero Ímpar e Positivo')

