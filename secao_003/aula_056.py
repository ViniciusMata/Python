"""
split e join com list e str
split - divide uma string
join  - une uma string
"""

frase = '   Olhá só que  , coisa interessante'

lista_frase_original = frase.split(',')
lista_frase_corrigido = []

for i, frase in enumerate(lista_frase_original):
    lista_frase_corrigido.append(lista_frase_original[i].strip())

print(lista_frase_original)
print(lista_frase_corrigido)

print()

frases_unidas = ', '.join(lista_frase_corrigido)
print(frases_unidas)