'''6.Faça um programa que leia 5 números e informe a soma e a média dos números'''

numeros = []
for i in range(1, 6):
    numeros.append(int(input(f'Digite o {i}º numero: ')))
print(f'A soma dos numeros é: {sum(numeros)} \nA média dos numeros é: {sum(numeros)/5} ')