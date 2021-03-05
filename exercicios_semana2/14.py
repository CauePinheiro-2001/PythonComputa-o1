'''14.Sabe-se que para iluminar de maneira correta os cômodos  de  uma  casa,
para  cada  m2  deve-se usar 18W de potência.
Faça um programa que recebe as duas dimensões de um cômodo  em metros),
calcule e mostre a sua área (em m2) e a potência de iluminação que deverá ser usada.'''

print('Programa 14')
comprimento = float(input('Comprimento do cômodo da casa em metros:'))
largura = float(input('Largura do comôdo da casa em metros: '))
areacomodo = largura * comprimento
print('A area do cômodo é : {0}m²'.format(areacomodo))
print('Potência que deverá ser usada para iluminação: {0}W'.format(areacomodo*18))