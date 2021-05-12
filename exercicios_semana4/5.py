''' 5.Faça um Programa que leia um número e exiba o dia correspondente da
semana. (1-Domingo, 2-Segunda, etc.), se digitar outro valor deve
aparecer valor inválido.'''

numero = int(input('Insira um número: '))
if numero == 1:
    print('O dia da semana que esse numero corresponde é: Domingo')
elif numero == 2:
    print('O dia da semana que esse numero corresponde é: Segunda')
elif numero == 3:
    print('O dia da semana que esse numero corresponde é: Terça')
elif numero == 4:
    print('O dia da semana que esse numero corresponde é: Quarta')
elif numero == 5:
    print('O dia da semana que esse numero corresponde é: Quinta')
elif numero == 6:
    print('O dia da semana que esse numero corresponde é: Sexta')
elif numero == 7:
    print('O dia da semana que esse numero corresponde é: Sábado')
else:
    print('Valor INVÁLIDO: .')



