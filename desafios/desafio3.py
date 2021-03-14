from random import randint
print('1=Tesoura, 2=Papel, 3=Pedra')
escolha = int(input('Sua escolha: '))
computador = randint(1,3)
print('Escolha do computador: ', computador)

if escolha == 1 and computador == 1:
    print('Você escolheu: Tesoura \nO computador escolheu: Tesoura \nEmpate')
elif escolha == 2 and computador == 2:
    print('Você escolheu: Papel \nO computador escolheu: Papel \nEmpate')
elif escolha == 3 and computador == 3:
    print('Você escolheu: Pedra \nO computador escolheu: Pedra \nEmpate')
elif escolha == 1 and computador == 2:
    print('Você escolheu: Tesoura \nO computador escolheu: Papel \nVocê ganhou!')
elif escolha == 1 and computador == 3:
    print('Você escolheu: Tesoura \nO computador escolheu: Pedra \nVocê perdeu!')
elif escolha == 2 and computador == 1:
    print('Você escolheu: Papel \nO computador escolheu: Tesoura \nVocê perdeu')
elif escolha == 2 and computador == 3:
    print('Você escolheu: Papel \nO computador escolheu: Pedra \nVocê ganhou!')
elif escolha == 3 and computador == 1:
    print('Você escolheu: Pedra \nO computador escolheu: Tesoura \nVocê ganhou')
elif escolha == 3 and computador == 2:
    print('Você escolheu: Pedra \nO computador escolheu: Papel \nVocê perdeu!')
else:
    print('Numero invalido')



