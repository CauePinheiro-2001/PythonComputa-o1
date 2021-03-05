'''10.Faça um programa que leia quatronotas obtidas por um aluno na disciplina de Cálculo.
Calcule a média das notas. Se a média for superior a 6 imprima “APROVADO”.'''

print('Programa 10')
a = float(input('Primeira Nota: '))
b = float(input('Segunda Nota: '))
c = float(input('Terceira Nota: '))
d = float(input('Quarta Nota: '))

media = (a+b+c+d)/4

if media >= 6:
    print('Aprovado, nota final: ', media)
else:
    print('Reprovado, nota final: ', media)