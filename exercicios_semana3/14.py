'''14.Faça  um  algoritmo  que  leia  2  valores  inteiros (X, Y).
Pedir para que o usuário escolha entre ordem crescente, 1,ou decrescente, 2.
Ordenar conforme solicitação do usuárioe imprimir.'''

print('Programa 14')

x = int(input('Primeiro valor inteiro: '))
y = int(input('Segundo valor inteiro: '))
escolha = int(input('Digite 1 para colocar em ordem crescente e 2 para ordem decrescente: '))
if escolha == 1 and x > y:
    print('A oredem crescente é: {0},{1} '.format(y,x))
elif escolha == 1 and y > x:
    print('A ordem crescente é: {0},{1}'.format(x,y))
elif escolha == 2 and x > y:
    print('A ordem decrescente é: {0},{1}'.format(x,y))
else:
    print('A ordem decrescente é: {0},{1}'.format(y,x))


