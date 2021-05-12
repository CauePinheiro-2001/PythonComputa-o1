'''8.Faça um programa que leia e valide as seguintes informações:
a.Idade: entre 0 e 100;
b.Salário: maior que zero;
c.Sexo: 'f' ou 'm';
d.Estado Civil: 's', 'c', 'v', 'd'
'''

idade = int(input('Idade (entre 0 e 100): '))
while 0 > idade or 100 < idade:
    idade = int(input('Idade inválida, insira a idade novamente: '))
salario = int(input('Salario (maior que zero): '))
while salario < 0:
    salario = float(input('Salário inválido, insira o salário novamente: '))
sexo = input('Sexo (f ou m): ')
while sexo != 'f' and sexo != 'm':
    sexo = input('Sexo inválido, insira o sexo novamente: ')
estado_civil = input('Estado civil (s, c, v, d): ')
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input('Estado Cívil inválido, insira novamente: ')

from datetime import datetime
tempo_atual = datetime.now()
print('Valores validados em {0}/{1}/{2} {3}:{4}h '.format(tempo_atual.day, tempo_atual.month,
tempo_atual.year, tempo_atual.hour, tempo_atual.minute))
print('Os valores são: ')
print('Idade: ', idade)
print('Saário: ', salario)
print('Sexo: ', sexo)
print('Estado Civil: ', estado_civil)