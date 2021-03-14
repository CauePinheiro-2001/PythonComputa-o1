import random   # importa as funções do random
megasena = list(range(1,61))  # Criar uma lista de com os numeros sa megasena
sorteados = []  # Criar lista vazia de numeros sorteados
nossos_num = []  # Criar lista vazia dos nossos numeros
mega_sort = megasena

#1- realização dos sorteios

for i in range(1, 7):  #As seguintes condições vão se repetir 6 vezes:
    sorteio = random.choice(mega_sort) #escolher um numero aleatorio de mega_sort
    sorteados.append(sorteio) #adionar o numero sorteado na lista sorteados
    mega_sort.remove(sorteio) #Remover o numero sorteado da lista mega_sort

for i in range(1, 7): #As seguintes condições vão se repetir 6 vezes:
    numero = int(input("informe o {0}° número: ".format(i))) #Escolher os numeros e apresenta-los
    nossos_num.append(numero) #Adicionar o nosso numero na lista

#2- verificação dos acertos:
print('------------VERIFICAÇÃO-------------')
nossos_num.sort() # Colocar a lista em ordem crescente
sorteados.sort() # Colocar a lista em ordem crescente
acertos = (set(sorteados).intersection(nossos_num)) #Acertos é a intersecção das duas listas
num_acertos = len(set(sorteados).intersection(nossos_num)) #Quantidade de numeros da intersecção das listas

if nossos_num == sorteados:
    print('Parabéns você é um milionário, você acertou os 6 números')
    print('Os numeros sorteados foram: ', sorteados)
    print('Os numeros acertados foram: ', nossos_num)
elif num_acertos == 0:
    print('Não foi dessa vez, você errou os 6 números')
    print('Os numeros sorteados foram: \n{0}'.format(sorteados))
    print('Você não acertou nenhum numero')
else:
    print('Não foi dessa vez, você acertou {0} números'.format(num_acertos))
    print('Os numeros sorteados foram: \n{0}'.format(sorteados))
    print('Os numeros acertados foram: \n{0}'.format(acertos))

