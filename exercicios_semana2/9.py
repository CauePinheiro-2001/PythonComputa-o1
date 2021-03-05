'''9.Faça um programa para ler dois valores (altura e  raio  de  um  cilindro),
calcular  e  mostrar  o volumee área. (A= π∙r2)(V = π∙r2∙h).'''

print('Programa 9')
h = float(input('Altura do cilindro: '))
r = float(input('Raio do cilindro: '))
a = 3.14*(r**2)
v = 3.14*(r**2)*h
print(' A área do cilindro é: {0} \n O volume do cilidro é: {1}'.format(a,v))