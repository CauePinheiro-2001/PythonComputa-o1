'''5.Faça um programa que peça 10 números inteiros, calcule e
mostre a quantidade de números pares e a quantidade de números impares'''
pares = []
impares = []
numeros = []

for i in range(1, 11):
    numeros.append(int(input(f'Digite o {i}º numero inteiro: ')))
for numero in numeros:
    if (numero % 2) == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'Os numeros pares são: {pares} \nOs numeros ímpares são: {impares}')
print(f'Temos um total de {len(pares)} numeros pares. \nTemos um total de {len(impares)} numeros ímpares.')
