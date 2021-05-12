'''2.As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contraram para desenvolver o programa que calculará
os reajustes.
•Faça um programa que recebe o salário de um colaborador
e o reajuste segundo o seguinte critério, baseado no salário atual:
•salários até R$280.00 (incluindo): aumento de 20%
•salários entre R$280.00 e R$700.00: aumento de 15%
•salários entre R$700.00 e R$1500.00: aumento de 10%
•salários de R$1500.00 em diante: aumento de 5%
Após o aumento ser realizado, informe  na tela:
•o salário antes do reajuste;
•o percentual de aumento aplicado;
•o valor do aumento;
•o novo salário, após o aumento'''

salario = float(input('Digite o salario do colaborador: '))

if 280 >= salario:
    salario20 = salario*1.2
    diferenca1 = salario20 - salario
    print('O salario antes do reajuste: ', salario)
    print('Aumento de 20%')
    print('O salario com reajuste é: ', salario20)
    print('O valor do aumento é: ', diferenca1)
elif 280 > salario >= 700:
    salario15 = salario*1.15
    diferenca2 = salario15 - salario
    print('O salario antes do reajuste: ', salario)
    print('Aumento de 15%')
    print('O salario com reajuste é: ', salario15)
    print('O valor do aumento é: ', diferenca2)
elif 700 > salario >= 1500:
    salario10 = salario*1.1
    diferenca3 = salario10 - salario
    print('O salario antes do reajuste: ', salario)
    print('Aumento de 10%')
    print('O salario com reajuste é: ', salario10)
    print('O valor do aumento é: ', diferenca3)
else:
    salario5 = salario*1.05
    diferenca4 = salario5 - salario
    print('O salario antes do reajuste: ', salario)
    print('Aumento de 5%')
    print('O salario com reajuste é: ', salario5)
    print('O valor do aumento é: ', diferenca4)
