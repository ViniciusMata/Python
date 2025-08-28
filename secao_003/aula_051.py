"""
Introdução ao desempacotamento + tuples (tuplas)
"""

nomes = ['Maria', 'Helena', 'Luiz']

nome1, nome2, nome3 = nomes
print(nome1)

print('***************************')

nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome2)

print('***************************')

_, _, nome3, *resto = ['Maria', 'Helena', 'Luiz'] #OR *_, nome3 = ['Maria', 'Helena', 'Luiz'] 
print(nome3)