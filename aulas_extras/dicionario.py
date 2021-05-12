'''Dicionários'''

#estrutura:
ete = {'cor': 'verde', 'pontos': 5, 'velocidade': 'medio'}

#Chamar um valor do dicioário:
print(ete['cor'])

#Acrescentar valores:
ete['posiçãox'] = 0
ete['posiçãoy'] = 25
print(ete)

#modificando valores:
ete['cor'] = 'amarelo'
print(ete)

#Velocidade exemplo:
if ete['velocidade'] == 'lento':
    x_incremento = 1
elif ete['velocidade'] == 'medio':
    x_incremento = 2
else:
    x_incremento = 3

ete['posiçãox'] = ete['posiçãox'] + x_incremento
print('Nova posição: ' + str(ete['posiçãox']))

#Removendo valores:
del ete['velocidade']
print(ete)

#Percorrendo todos os pares:
for chave, valor in ete.items():
    print("\nChave: ", chave)
    print('Valor: ', valor)

#Uma lista de dicionários:
darius = {'dano': 'físico', 'posição': 'top'}
rengar = {'dano': 'físico', 'posição': 'selva'}
mf = {'dano': 'físico ou mágico', 'posição': 'atirador'}
campeoes = [darius, rengar, mf]
for campeao in campeoes:
    print(campeao)

#Criando frota:
soldados =[]
for soldado in range(30):
    novo_soldado = {'Altura': '1,80', 'Peso': '80', 'Caracteristica': 'Atirador/Lutador'}
    soldados.append(novo_soldado)
#Mostrando os cinco primeiros
for soldado in soldados[:5]:
    print(soldado)
print('...')
#Mostrar quantos soldados foram criados:
print(f'Foram convocados {len(soldados)} soldados pra essa missão')

#Enquete com mais de uma opção:
enquete = {
    'Caue': ['Python', 'CSS', 'HTML'],
    'Gabi': 'Python'
}
print(enquete)



