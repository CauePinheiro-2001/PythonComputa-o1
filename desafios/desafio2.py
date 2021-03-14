preco = int(input('Preço do produto: '))
codigo = int(input('Código de origem: '))

if codigo == 1:
    print('Preço: {0}, Código de Origem: 1, Procendência: Sul'.format(preco))
elif codigo == 2:
    print('Preço: {0}, Código de Origem: 2, Procendência: Norte'.format(preco))
elif codigo == 3:
    print('Preço: {0}, Código de Origem: 3, Procendência: Leste'.format(preco))
elif codigo == 4:
    print('Preço: {0}, Código de Origem: 4, Procendência: Oeste'.format(preco))
elif codigo >= 5 and codigo <= 6:
    print('Preço: {0}, Código de Origem: {1}, Procendência: Nordeste'.format(preco, codigo))
elif codigo >= 7 and codigo <= 9:
    print('Preço: {0}, Código de Origem: {1}, Procendência: Sudeste'.format(preco, codigo))
elif codigo >= 10 and codigo <= 20:
    print('Preço: {0}, Código de Origem: {1}, Procendência: Centro-Oeste'.format(preco, codigo))
elif codigo >= 25 and codigo <= 30:
    print('Preço: {0}, Código de Origem: {1}, Procendência: Nordeste'.format(preco, codigo))
else:
    print('Produto importando, Preço: ', preco)

