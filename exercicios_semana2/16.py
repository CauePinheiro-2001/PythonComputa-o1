'''16.Escreva um programa que leia dois números que deverão ser colocados, respectivamente, nas variáveis vA e vB.
O programa deve, então, trocar os valores de vA por vBe  vice-versa e mostrar o conteúdo destas variáveis.'''

print('Programa 16')
vA = float(input('Valor de vA: '))
vB = float(input('Valor de vB: '))
x = vA
y = vB
vA = y
vB = x
print ('Valores invertidos: \n Valor  de vA: {0} \n Valor de vB: {1}'.format(vA,vB))

