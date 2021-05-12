''''''

#Laço while
#variavel = 1
#while variavel <= 5:
#    print(variavel)
#    variavel += 1

#prompt = '\nFale algo e eu vou repetir para você'
#prompt += '\nDigite "sair" para encerrar o programa.'
#mensagem = ''
#while mensagem != 'sair':
#    mensagem = input(prompt)
#    print(mensagem)

#Usando uma flag
#flag = True
#while flag:
#    mensagem = input(prompt)
#    if mensagem == 'sair':
#        flag = False
#    else:
#        print(mensagem)

#Usando break para sair de um laço:
#conteudo = '\nDigite o nome da sua cidade,'
#conteudo += '\nou "sair" para encerrar o programa: '
#while True:
#    cidade = input(conteudo)
#    if cidade == 'sair':
#        break
#    else:
#        print('Eu amo ir para ' + cidade.title() + '!')

#Usando continue em um laço: Ignore e continue.
numero = 0
while numero < 10:
    numero = numero + 1
    if numero % 2 == 0:
        continue
    print(numero)