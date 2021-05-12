def localizaMaior(matriz):
    linha = 0
    linhaMaior = 0
    colunaMaior = 0
    maior = matriz[0][0]
    while linha < 4:
        coluna = 0
        while coluna < 4:
            if maior < matriz[linha][coluna]:
                maior = matriz[linha][coluna]
                linhaMaior = linha
                colunaMaior = coluna
            coluna = coluna + 1
        linha = linha + 1
    print(matriz)
    print('O maior elemento da matriz é ', maior)
    print('Está localizado na posição ', linhaMaior, colunaMaior)
