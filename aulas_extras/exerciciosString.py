'''Mensagem Pessoal: Armazene o nome de uma pessoa em uma variável e
apresente uma mensagem a essa pessoa. Sua mensagem deve ser simples:
(Alô Fulano, você gostaria de aprender um pouco de Python hoje?'''

nome = 'Cauê'
print('Alô '+ nome + ' você gostaria de aprender um pouco de  Python hoje?')

'''Letras maiúsculas e minúsculas em nomes: armazene o 
nome de uma pessoa em uma variável e então apresente o nome 
dessa pessoa em letras maiúsculas e minúsculas, e somente 
com a primeira letra maiúscula.'''

name = 'cauê pinheiro'
print(name)
print(name.upper())
print(name.title())

'''Citação Famosa: Encontre uma citação de uma pessoa famosa que 
você admire. Exiba a citação e o nome do autor. Sua saída deverá ter 
a seguinte aparência, incluindo as aspas: FULANO certa vez disse:'Frase'
'''

print('Rigolon certa vez disse: "Eu te amo muito"')

'''Removendo caracteres em branco de nomes: Armazene o nome de uma pessoa e inclua
caracteres em branco no início e no final do nome, lembre-se de usar \ t e \ n. 
Exiba utilizando as funções: lstrip(), rstrip(), strip(). '''

espacos = '    caue pinheiro     '
print(espacos)
print(espacos.lstrip())
print(espacos.rstrip())
print(espacos.strip())

