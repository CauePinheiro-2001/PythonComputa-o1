'''6.Escreva  um  programa  que  lê  um  número  real.
Informe se o número é maior ou igual a 100, se está entre
51 e 99 ou se é menor ou igual a 50.'''

print('Programa 6')
x = int(input('Informe um valor para o programa ser realizado: '))
if x >= 100:
    print('Esse numero é maior ou igual a 100')
elif x >= 51 and x <= 99:
    print('Esse numero está entre 51 e 99')
else:
    print('Esse número é menor que 50')
