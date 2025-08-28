"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimanl (ABCDEF0123456789)
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o numero aparecer antes dos zeros
Sinal + ou -
Ex.: 0>-100, 1.f
Conversion flags !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1051.909898:0=+10,.2f}')
print(f'O hexadecimal de 1500 é {1500:08X}')