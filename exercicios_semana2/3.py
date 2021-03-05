'''3.Escreva   um   programa   para   ler,   calcular   e
escrever a média aritméticaentre dois números.'''

print('Programa 3')

print('Média aritmética')
print("POR FUNÇÃO")
def mediaaritmetica(valor1,valor2):
    m = (valor1 + valor2) / 2
    print('A média aritmética é : {0}'.format(m))
print(mediaaritmetica(10,5))

print("POR VARIAVEl")
a = float(input('Valor 1: '))
b = float(input('Valor 2: '))
c = (a + b)/2
print('A média aritmética é : {0}'.format(c))
