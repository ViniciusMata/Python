"""
Iterando strings com while
"""

nome = 'Vinicius Mata'

x = 0
novo_nome1 = ''
novo_nome2 = ''

while x < len(nome):
    letra = nome[x]
    novo_nome1 = novo_nome1 + letra + '*'
    novo_nome2 += f'*{letra}'
    x += 1

print(f'{novo_nome1=}')
print(f'{novo_nome2=}')