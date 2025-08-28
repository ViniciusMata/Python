"""
enumerate - enumera iteráveis (indices)
"""

#[(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

print('*************************')
for indice, nome in enumerate(lista):
    print(indice, nome)

#print('*************************')
#lista_enumerada = enumerate(lista)
#for item in enumerate(lista):
#    indice, nome = item
#    print(indice, nome)

#print('*************************')
#for tupla_enumerada in enumerate(lista):
#    print('FOR da tupla:')
#    for valor in tupla_enumerada:
#        print(f'\t{valor}')