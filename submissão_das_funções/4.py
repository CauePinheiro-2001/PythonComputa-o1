def mediaNotas(lista, quantidade):
    '''Apresenta a média das notas abaixo de 6,
     e apresenta as notas abaixo de 6'''
    notas_abaixo_média = []
    for i in lista:
        if i < 6:
            print(i)
            notas_abaixo_média.append(i)
    if len(notas_abaixo_média) != []:
        print(f'A média das notas abaixo de 6 foi =  {sum(notas_abaixo_média)/len(notas_abaixo_média)}')
    else:
        print('Não existe notas abaixo de 6')