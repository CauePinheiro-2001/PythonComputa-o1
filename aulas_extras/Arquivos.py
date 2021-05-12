'''Crianção de Arquivos'''

#criando um arquivo
#with open ('Impares.txt', 'w') as impares:
#    with open ('Pares.txt', 'w') as pares:
#        for n in range(0, 500):
#            if n % 2 == 0:
#                pares.write(f'{n}\n')
#            else:
#                impares.write(f'{n}\n')


#leitura e escrita:
#with open ('multiplos_4.txt', 'w') as multiplos4:
#    with open('Pares.txt') as pares:
#        for l in pares.readlines():
#            if int(l) % 4 == 0:
#                multiplos4.write(l)


#Processamento de um arquivo
#with open('entrada.txt', 'w') as entrada:
#    entrada.write(';Esta linha não deve aparecer\n')
#    entrada.write('>Esta linha deve ser impressa a direita\n')
#    entrada.write('*Esta linha deve ser centralizada\n')
#    entrada.write('Uma linha normal\n')
#    entrada.write('Outra linha normal')
#largura = 79
#with open('entrada.txt') as entrada:
#    for linha in entrada.readlines():
#        if linha[0] == ';':
#            continue
#        elif linha[0] == '>':
#            print(linha[1:].rjust(largura))
#        elif linha[0] == '*':
#            print(linha[1:].center(largura))
#        else:
#            print(linha)

