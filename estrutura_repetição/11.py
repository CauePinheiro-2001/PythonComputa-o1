'''12.Supondo que a população de um país A seja da ordem de 80000
habitantes com uma taxa anual de  crescimento  de  3%  e  que  a
população  de  B  seja  200000  habitantes  com  uma  taxa  de
crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento'''

populacaoA = 80000
populacaoB = 200000
anos = 0

while populacaoA < populacaoB:
    populacaoA = populacaoA * 1.03
    populacaoB = populacaoB * 1.015
    anos = anos + 1

print('A quantidade de anos necessários para que a popução de A seja maior que de B são: ', anos)



