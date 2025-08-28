"""
Tipo Tupla - Um lista imutável. Para fazer uma tupla basta não inicar com [], logo pode iniciar com () ou sem ().
"""

#Isso é uma tupla
nome0 = 'Maria', 'Helena', 'Luiz'
print(nome0)

print('**************************')

#Converter uma lista em tuple
nome1 = ['João', 'José', 'Lucas']
nome1 = tuple(nome1)
print(nome1)

print('**************************')

#Converter uma tuple em lista
nome2 = ('Sara', 'Sandra', 'Lucia')
nome2 = list(nome2)
print(nome2)