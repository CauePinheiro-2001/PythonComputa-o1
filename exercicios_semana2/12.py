'''12.O salário total do vendedor é o seu salário fixo +
percentual sobre as vendas: escrevaum programa  que lê o
Id do vendedor, o salário fixo, o valor das vendas  por
ele efetuadase o percentual que ganha sobre essas vendas.
 Imprimir o Iddo vendedor e o salário total.'''

print('Progama 12')
idvendedor = int(input('Id vendedor: '))
salariofixo = float(input('Salario fixo: '))
valorvendas = float(input('Valor das vendas: '))
percentual = float(input("percentual das vendas: "))
salariofinal = salariofixo + (valorvendas*percentual)
print("Salario do vendedor de id {0} é: {1}: ".format(idvendedor, salariofinal))