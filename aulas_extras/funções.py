'''Funções são tem diferentes finalidades para que programador decida qual seja:'''

#Estrutura da função:
def ola_mundo():
    '''Diz olá mundo'''
    print('Olá mundo!')
ola_mundo()

def saudacao(nome='caue'):
    '''Exibe uma saudação simples ao usuário'''
    print(f'Olá {nome.title()}!')

saudacao('Gabriela')

def objeto(cor_do_objeto,tamanho_do_objeto):
    print(f'A cor do objeto é: {cor_do_objeto} \nO tamanho do objeto é: {tamanho_do_objeto}')

objeto('azul','Pequeno')

#Para funções que tem parametros podemos utilizar, o return:
def parabens(fulano):
    parabens_fulano = 'Parabens ' + fulano
    return parabens_fulano
print(parabens('caue'))

#função de tempo atual:
from datetime import datetime
def tempo_atual():
    '''Busca a data e hora. Lembre-se de utilizar a biblioteca datetime: from datetime import datetime'''
    tempo_atual = datetime.now()
    print('tempo atual : {0}/{1}/{2} as {3}:{4}h'.format(tempo_atual.day, tempo_atual.month,
    tempo_atual.year, tempo_atual.hour, tempo_atual.minute) )

tempo_atual()