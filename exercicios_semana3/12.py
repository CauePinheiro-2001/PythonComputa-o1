'''12.Faça um programa que leia quatronotas obtidas por um aluno na disciplina de Cálculo.
Calcule a média das notas. Se a média for superior a 6 imprima  “APROVADO”;
se  a  média  estiver entre  5  e  6 imprima “DEPENDÊNCIA”;
se a média   for   inferior ou   igual a   5   imprima “REPROVADO”.'''

print('Programa 12')

a = float(input('Primeira Nota: '))
b = float(input('Segunda Nota: '))
c = float(input('Terceira Nota: '))
d = float(input('Quarta Nota: '))

media = (a+b+c+d)/4

if media > 6:
    print('Aprovado, nota final: ', media)
elif 5 <= media <= 6:
    print('Dependência, Nota entre ou igual 5 e 6.')

else:
    print('Reprovado, nota final: ', media)