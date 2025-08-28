"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimanl (ABCDEF0123456789)
"""

nome = 'Vinicius'
preco1 = 100.21312356
preco2 = 5985134
variavel = '%s, o preço é €%.2f' % (nome, preco1)
print(variavel)
print('O hexadecimanal de %f é %X' % (preco2, preco2))