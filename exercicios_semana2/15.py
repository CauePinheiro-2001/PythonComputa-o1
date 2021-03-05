'''15.Façaum programa que leia o número do funcionário, o número de horas trabalhadas mensais,
o valor que recebe por hora e o número de filhos com idade menor de 14 anos.
Calcular e escrever o salário deste funcionário,
sendo que cada filho menor de 14 anos acrescenta 10% do salário.'''

print('Programa 15')
numerofuncionario = int(input('Numero do funcionário: '))
horastrabalhadas = float(input('Horas trabalhadas: '))
valorhora = float(input('Valor da hora: '))
filhos = int(input("Numero de filhos com menos de 14 anos: "))
salarioinicial = horastrabalhadas*valorhora
porcentagem = (filhos * 0.1) * salarioinicial
salariofinal = salarioinicial + porcentagem
print('O salario desse funcionario é: ', salariofinal)

