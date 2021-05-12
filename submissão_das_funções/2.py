def exibeNotasInvertido(lista, quantidade):
    '''Exibe notas em ordem invertida em linhas diferentes
    e a quantidade de numeros pares'''
    parametro = len(lista) - 1
    lista_invertida = []
    numeros_pares = []
    while parametro >= 0:
        print(lista[parametro])
        if lista[parametro] % 2 == 0:
            numeros_pares.append(lista[parametro])
        parametro = parametro - 1
    return print(f'A quantidade de números pares da lista é =  {len(numeros_pares)}')