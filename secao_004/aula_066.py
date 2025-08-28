"""
Argumentos nomeados e nao nomeados em funcoes
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeados recebe apenas o argumento (valor)
"""

def soma(x, y):
    print(f'{x=} {y=}', '|', 'x + y = ', x + y)

soma(1, 2)     #Argumento não nomeado / posicionais
soma(x=1, y=2) #Argumento nomeado
soma(x=2, y=4) #Argumento nomeado
