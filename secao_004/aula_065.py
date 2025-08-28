"""
Introdução as funcoes (def) em Python
Funcções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem recber valores para parametros (argumentos)
e retornar um valor especifico.
Por padrão, funções Python retornam None (nada)
"""

def exiba1():
    print('Olá Mundo')

def exiba2(a, b, c):
    print(f'Arg1.: {a}, Arg2.: {b}, Arg3.: {c}')

exiba1()

exiba2(1, 2, 3)

