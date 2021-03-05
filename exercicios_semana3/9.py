'''9.Certa empresa de transporte fornece um serviço que custa R$ 100,00.
Para idosos (idade acima de 65) OU para crianças (idade abaixo de 18) a
empresa oferece desconto de R$ 20 neste serviço.
Peça para que o usuário  informe  sua idade e, se possível, calcule e   aplique o desconto.
Imprima  o  valor  a  ser  pago  pela passagem, se  foi possível aplicar o desconto e qual o valor do mesmo.'''

print('Programa 9')
x = int(input('Qual a sua idade: '))
if x > 65 or x < 18:
    print('Valor da passagem: R$100,00 \nDesconto na passagem: R$20,00 \nTotal a pagar: R$80,00')
else:
    print('Valor da passagem: R$100,00 \nTotal a pagar: R$100,00')
