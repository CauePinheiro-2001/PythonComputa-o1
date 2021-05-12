'''Nomes: armazene nomes de alguns colegas seus em uma lista e apresente
o nome deles um por um em linhas diferentes'''

amigos = ['Amor', 'Christian', 'Douglas', 'Andreia', 'Bruna']
for amigo in amigos:
    print(amigo)

'''Saudações: use o exercicio anterior, mas em vez de exibir somente
o nome de cada colega, apresente um mensagem para eles.'''

for amigo in amigos:
    print('Estou com muita saudade,',amigo)

'''Convide seus amigos para uma festa, sabendo que deve chamar mais algum amigo, pois
um dos seus amigos anteriores não poderá comparecer.'''


amigos[0] = 'Gabriela'
for amigo in amigos:
    print('Venha para minha festa,', amigo)

'''Chame mais 3 colegas para essa festa '''

amigos.append('Ruly')
amigos.append('Caio')
amigos.append('Cauê')
for amigo in amigos:
    print('Venha para minha festa,', amigo)

'''Adicione um colega no inicio da sua lista'''

amigos.insert(0, 'Larissa')
print(amigos)

