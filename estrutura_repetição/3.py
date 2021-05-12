'''3.Faça um programa que leia 5 números e informe o maior número.'''

numeros = []
for i in range(1, 6):
    numeros.append(int(input(f'Digite o {i}º numero: ')))
print('O maior entre eles é: ', max(numeros))



