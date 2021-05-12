'''3.Faça um programa que lê as duas  notas  parciais obtidas
por um aluno numa disciplina ao longo de um semestre, e
calcule  a  sua  média. A atribuição de conceitos obedece
à tabela abaixo:
Média de Aproveitamento   Conceito
•Entre 9.0 e 10.0            A
•Entre 7.5 e 9.0             B
•Entre 6.0 e 7.5             C
•Entre 4.0 e 6.0             D
•Entre 4.0 e zero            E

O algoritmodeve mostrar na tela as notas, a média, o conceito
correspondente e a mensagem “APROVADO” se o conceito for A,  B
ou C ou “REPROVADO” se o conceito for D ou E.'''

x = int(input('Quantas avalições tiveram no semestre: '))
notas = []

for i in range(x):
    notas.append(float(input(f"Digite a nota da {i+1}ª avaliação: ")))
    if notas[-1] > 10 or notas[-1] < 0:
        notas.pop()
        print('Valor INVÁLIDO digite novamente a nota.')
        notas.append(float(input(f"Digite a nota da {i+1}ª avaliação novamente")))


media = sum(notas) / x

if 9 <= media <= 10:
    print('Seu conceito foi A \nAprovado!')
elif 7.5 <= media < 9:
    print('Seu conceito foi B \nAprovado!')
elif 6 <= media < 7.5:
    print('Seu conceito foi C \nAprovado!')
elif 4 <= media < 6:
    print('Seu conceito foi D \nReprovado!')
else:
    print('Seu conceito foi E \nReprovado!')




