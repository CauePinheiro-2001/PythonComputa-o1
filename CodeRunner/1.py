matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
def preencheMatriz(matriz):
    linha = 0
    while linha < 4:
        coluna = 0
        while coluna < 4:
            matriz[linha][coluna] = (linha*coluna)
            coluna = coluna + 1
        linha = linha + 1
preencheMatriz(matriz)
print(matriz)