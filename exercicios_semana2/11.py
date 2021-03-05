'''11.Construa um programa de venda de produto.
O programa deve: Informar dois  tipos  de  produto
e  seu  valor unitário (definido pelo programador);
Pedir para que o usuário informe quantas unidades do
produto 1 deseja obter; Pedir para que o usuário informe
quantas unidades do produto 2 deseja obter;
Calcular o valor total da compra
(produto 1 * valor unitário + produto 2 * valor unitário) e exibir o resultado.'''

# O comando print é utilizado para imprimir,
# ou seja, é um comando de saída.
print('Progama 11')
# O comando \n é utilizado para pular linhas
# na apresentação do terminal.
print('Loja: \n Mesa: R$500,00\n Cadeiras: R$130,00')
# Essas são variáveis em que o programador decide
# os valores e são armazenados
mesa = 500
cadeira = 130
# O comando input é utilizado para que os usuários
# consigam atribuir informações/dados/valores,.
# O input necessita que o pragramdor apresente o
# tipo de variável em alguns casos.
p1 = int(input('Quantas mesas você deseja : '))
p2 = int(input('Quantas cadeiras você deseja : '))
# O total é uma variável  que está sendo atribuida
# um cálculo utilazando das variáveis anteriores.
total = (mesa*p1) + (cadeira*p2)
# Quando utilizar uma variável no print, não pode
# estar entre aspas duplas ou simples como uma string.
print('Valor total da compra (R$): ', total)