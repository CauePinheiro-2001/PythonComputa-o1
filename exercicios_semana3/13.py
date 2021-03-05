'''13.Faça um programa que leia o número de presenças e quatro notas obtidas por um aluno na disciplina de Cálculo.
Calcule  a  média  das notas.
Se a média for superior a 6 E o aluno possuir 20 ou mais presenças imprima “APROVADO”;
se a média estiver entre 5 e 5.9 e o aluno possuir 20 ou mais presenças imprima “DEPENDÊNCIA”;
se o aluno possuir menos de 20 presenças OU média inferior a 5 imprima REPROVADO.'''

print('Programa 13')
presenca = int(input('Numero de presença do Aluno: '))

a = float(input('Primeira Nota: '))
b = float(input('Segunda Nota: '))
c = float(input('Terceira Nota: '))
d = float(input('Quarta Nota: '))

media = (a+b+c+d)/4

if media >= 6 and presenca >= 20:
    print('Aprovado')
elif 5 <= media <= 5.9 and presenca >= 20:
    print('Dependência')
elif presenca < 20:
    print('Reprovado por Presença')
else:
    print('Reprovado por Nota')

print('Sua media foi:', media)
