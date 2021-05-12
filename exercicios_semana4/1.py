'''1.Fazer um programa para ler um código (número inteiro) e
mostrar uma mensagem de acordo com a tabela abaixo.
Código        Mensagem
1             Grupo com 50% de promoção
3 ou 5        Grupo sem desconto
10 até 20     Grupo com 10% de desconto
outro         Código inválido'''

codigo = int(input('Escreva o código: '))
if codigo == 1:
    print('Grupo com 50% de promoção')
elif codigo == 3 or codigo == 5:
    print('Grupo sem desconto')
elif 10 <= codigo <= 20:
    print('Grupo com 10% de desconto')
else:
    print('Código Inválido')