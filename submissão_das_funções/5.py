def exibeNotasAcimaMedia(lista, quantidade):
    '''EXIBE NOTAS MAIORES QUE A MÉDIA E A QUANTIDADE DE NOTAS ACIMA DA MÉDIA.'''
    notas_maiores = []
    for valor in lista:
        if valor >= 6:
            print(valor)
            notas_maiores.append(valor)
    if notas_maiores != []:
        print(f'A média das notas acima de 6 é =  {sum(notas_maiores)/len(notas_maiores)}')