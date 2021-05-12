'''7.Faça um programa que leia um nome de usuário e a sua
senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.'''
print('Crie seu cadastro')
login = input('Digite seu login: ')
senha = input('Digite sua senha: ')
while login == senha:
    print('Não é permitido que o login seja igual a senha')
    senha = input('Digite sua senha novamente: ')
from datetime import datetime
tempo_atual = datetime.now()
print('Cadastro realizado com sucesso em : {0}/{1}/{2} as {3}:{4}h'.format(tempo_atual.day, tempo_atual.month,
tempo_atual.year, tempo_atual.hour, tempo_atual.minute) )