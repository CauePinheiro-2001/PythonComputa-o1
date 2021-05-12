'''4.Faça um programa que leia um número e imprima sua tabuada (de 1 até 10)'''

x = int(input('Escolha um numero e veja sua tabuada: '))
for i in range(1 ,11):
    print(f'{x} x {i} =', x * i )