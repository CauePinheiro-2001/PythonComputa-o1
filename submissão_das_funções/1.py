def exibeNotas(lista, quantidade):
    '''Exibe notas e quantidade de números ímpares'''
    numeros_impares = []
    for i in lista:
        print(i)
        if i % 2 != 0:
            numeros_impares.append(i)
    return print(f'A quantidade de números ímpar da lista é =  {len(numeros_impares)}')