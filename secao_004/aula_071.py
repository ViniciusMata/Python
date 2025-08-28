"""
args - Argumentos nao nomeados
* - *args (empacotamento e desempacotamento)
"""

#Lembrete de desempacotamento
#x, y, *resto = 1, 2, 3, 4
#print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

somaNum = soma(1, 2, 3, 4, 5, 6)
print(somaNum)