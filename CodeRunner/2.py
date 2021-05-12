def localizaValor(matriz,valor):
    linha = 0
    encontrado = 0
    print(matriz)
    print('O valor que está sendo procurado é: ', valor)
    while linha < 5:
        coluna = 0
        while coluna < 5:
            if matriz[linha][coluna] == valor:
                print('Encontrado na posição: ', linha, coluna)
                encontrado = 1
            coluna = coluna + 1
        linha = linha + 1

    if encontrado == 0:
        print('Elemento não encontrado')