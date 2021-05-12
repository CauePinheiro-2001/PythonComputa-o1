'''11.Em uma eleição existem 4 candidatos. Os votos são informados
por código (de 1 a 4). Os dados utilizados para a contagem de votos,
obedecem ao seguinte:
a.1, 2, 3, 4 = votos para os respectivos candidatos
b.5 = voto nulo
c.6 voto em branco
Escreva um programa que calcule e escreva (até o usuário digitar o número 0 para sair):
O total de votos para cada candidato
O total de votos nulo
O total de votos em branco
'''
candidato1 = []
candidato2 = []
candidato3 = []
candidato4 = []
voto_nulo = []
voto_branco = []
voto = 8
print('Digite 0 para encerrar a votação')
while voto != 0:
    voto = int(input('Digite seu voto: '))
    if voto == 1:
        candidato1.append(voto)
    elif voto == 2:
        candidato2.append(voto)
    elif voto == 3:
        candidato3.append(voto)
    elif voto == 4:
        candidato4.append(voto)
    elif voto == 5:
        voto_nulo.append(voto)
    elif voto == 6:
        voto_branco.append(voto)

print('Total de votos para o candidato 1: ', len(candidato1))
print('Total de votos para o candidato 2: ', len(candidato2))
print('Total de votos para o candidato 3: ', len(candidato3))
print('Total de votos para o candidato 4: ', len(candidato4))
print('Total de votos em branco: ', len(voto_branco))
print('Total de votos nulos: ', len(voto_nulo))

print('Programa encerrado')







