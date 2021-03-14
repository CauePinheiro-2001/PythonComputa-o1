'''String é o conjunto de caracteres e podem ser manipulados.'''

#Podemos fazer diversas modificações nas strings. vejamos algumas modificações:

name = 'caue pinheiro'
primeiro_nome = 'caue'
ultimo_nome = 'pinheiro'

# Colacar letras maiúsculas nas primeira letra de cada palavra:
print(name.title())

# Colocar todas as letras em maiusculas:
print(name.upper())

# Colocar todas as letras em minusculas:
print(name.lower())

# Concatena-las (juntando as strings):
full_name = primeiro_nome + ' ' + ultimo_nome
print(full_name.title())

# Tabulações (Paragrafos):
print('\tPython')

# Quebra de linha (Pular linha):
print('\nPython')

# Tabulaçõa com quebra de linha:
print('\n\tPython')

# Tirar espaços em branco do lado direito:
Py = 'Python '
print(Py.rstrip())

# Tirar os espaços em branco dos dois lados:
py = '  Python  '
print(py)
print(py.strip())
