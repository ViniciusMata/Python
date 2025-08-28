"""
Crie uma função que multiplica todos os argumentos nao nomeados recebidos
Retorne o total para uma variavel e mostre o valor da variavel
"""

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(10, 2, 3, 4, 5)
print(multiplicacao)

"""
Crie uma funcao que diga se o numero é par ou impar
Retorne se o numero é par ou impar
"""

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é PAR'
    return f'{numero} é ÍMPAR'

print(par_impar(1))
print(par_impar(2))
print(par_impar(3))
print(par_impar(4))
print(par_impar(5))
print(par_impar(6))
print(par_impar(7))
print(par_impar(8))
print(par_impar(9))
