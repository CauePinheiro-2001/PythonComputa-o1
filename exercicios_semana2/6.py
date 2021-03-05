'''6.Faça um programa no qual o usuário fornece os valores
de temperatura em Fahrenheit e o mesmo converte os valores para
Celsius Apresente o resultado.(C=(F-32)/1,8).'''

print('Programa 6')
f = float(input('Temperatura em Fahrenheit: '))
c = (f-32)/1.8
print('Temperatura em Celsius: ', round(c,2))