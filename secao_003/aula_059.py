"""
Desempacotamento em chamadas de métodos e funções
"""

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0
    ['Elaine'], #0
    # 0        1
    ['Maria', 'Helena'], #1
    # 0       1       2
    ['Luiz', 'João', 'Eduardar', (0, 5, 10, 15, 20)] #2
]

#p, b, *_, ap, u = lista
#print(p, u, ap)

#for nome in lista:
#    print(nome, end=' ')

#print(*lista)
#print(*tupla)

print(*salas, sep='\n')