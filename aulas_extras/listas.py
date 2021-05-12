'''LISTAS ARMAZENAM UM CONJUNTO DE IRFORMAÇÕES'''

# As listas são dessa maneira:
lista = ['item1', 'item2', 'item3', 'cauê']

# Acessar um item da lista:
print(lista[0], lista[1], lista[2])

# Acessar o ultimo item da lista:
print(lista[-1])

# Colocar a primeira letra de um item da lista em maiusculo:
print(lista[-1].title())

# Inserir um item em uma mensagem:
mensagem = 'Meu nome é ' + lista[-1].title() + ' Pinheiro'
print(mensagem)

# Modificando um item da lista:
lista[0] = 'modificado'
print(lista)

# Adicionar um item ao final da lista:
lista.append('Gabriela')
print(lista)

# Adicionar um item em qualquer posição da lista:
lista.insert(0,'primeiro_item')
print(lista)

# Remover um item da lista de posição conhecida:
del lista[0]
print(lista)

# O método pop tira o último item da lista, mas permite você trabalhar com ele porteriormente:
popped_lista = lista.pop()
print(lista)
print(popped_lista)

# O método pop para qualquer posição:
first_lista = lista.pop(0)
print(lista)
print(first_lista)

# String como o método pop:
mensagem2 = 'O item foi ' + first_lista.upper() + ' diversas vezes!'
print(mensagem2)

# Removendo um item pelo seu valor:
lista.remove('cauê')
print(lista)

# Removendo um item pelo seu valor em variável:
itemm = 'item3'
lista.remove(itemm)
print(lista)

# Organizando uma lista por ordem alfabética:
nomes = ['cauê', 'gabriela', 'andreia', 'bruna', 'douglas']
nomes.sort()
print(nomes)

# Organizando uma lista por ordem alfabética inversa:
nomes.sort(reverse=True)
print(nomes)

# Para preservar a ordem de uma lista, mas apresentar de forma ordenada:
print(sorted(nomes))

# Organizar uma lista de forma inversa:
nomes.reverse()
print(nomes)

# Descobrindo o tamanho de uma lista:
print(len(nomes))

# Exibir cada um dos itens de uma lista:
for nome in nomes:
    print(nome)

# Mais tarefas em um laço for:
for nome in nomes:
    print(nome.title() + ', Seja Bem Vindo(a) !!!')

# Após um lanço for: (repete uma vez)
for nome in nomes:
    print(nome.title() + ', Seja Bem Vindo(a) !!!')
    print('Repete sempre')
print('Repete uma vez')

# Criando lista numerica: (Note que a lista vai ser de 1 a 4)
numeros = list(range(1,5))
for numero in numeros:
    print(numero)
print(numeros)

# Mais uma informação sobre a função range:
pares = list(range(0, 11, 2))
print(pares)

# Podemos tambem:
quadrados = []
for quadrado in range(1, 11):
    expoente = quadrado**2
    quadrados.append(expoente)
print(quadrados)

# Colcando em uma linha:
quads = [quad2**2 for quad2 in range(1, 11)]
print(quads)

# Estatisticas simples de uma lista:
print(min(quadrados))
print(max(quadrados))
print(sum(quadrados))

# Copiando uma lista:
copia = quads[:]
print(copia)

# Intercção de listas:
numeros2 = list(range(1,11))
intersec = (set(numeros2).intersection(set(numeros)))
print(intersec)

# União de listas:
list_uniao1 = ['caue', 'gabi', 'um', 'perfeito']
list_uniao2 = ['e', 'são', 'casal']
list_uniao = (set(list_uniao1).union(set(list_uniao2)))
print(list_uniao)




