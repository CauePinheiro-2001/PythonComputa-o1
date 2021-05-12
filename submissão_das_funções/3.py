def somaNotas(lista, quantidade):
    '''A soma das notas maiores que a média e
     apresenta as notas maiores que a média'''
    notas_acima_media = []
    for i in lista:
        if i >= 6:
            print(i)
            notas_acima_media.append(i)
    return print(f'A soma das notas acima de 6 é =  {sum(notas_acima_media)}')