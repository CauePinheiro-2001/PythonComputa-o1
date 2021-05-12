def preencheMatrizNova(matrizA, matrizB):
    linha = 0
    matrizC = []
    while linha < 4:
        coluna = 0
        lista = []
        while coluna < 4:
            if matrizA[linha][coluna] > matrizB[linha][coluna]:
                lista.append(matrizA[linha][coluna])
            elif matrizA[linha][coluna] < matrizB[linha][coluna]:
                lista.append(matrizB[linha][coluna])
            else:
                lista.append(matrizA[linha][coluna])
            coluna = coluna + 1
        matrizC.append(lista)
        linha = linha + 1
    print('Matriz A =', matrizA)
    print('Matriz B =', matrizB)
    print('Matriz C = ', matrizC)