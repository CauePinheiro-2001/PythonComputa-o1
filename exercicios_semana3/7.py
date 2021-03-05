'''7.Escreva  um  programa  que  leia  dois  números inteiros.
Se o primeiro E o segundo valor forem positivos imprima “POSITIVO”;
se o primeiro E  o  segundo  valor  forem  negativos  imprima “NEGATIVO”,
caso     contrário     imprima“POSITIVO E NEGATIVO”. '''

print('Programa 7')
x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um valor inteiro: '))
if x >= 0 and y >= 0:
    print('POSITIVOS')
elif x < 0 and y < 0:
    print('NEGATIVOS')
elif x > 0 and y < 0:
    print('POSITIVO E NEGATIVO')
else:
    print('NEGATIVO E POSITIVO')

