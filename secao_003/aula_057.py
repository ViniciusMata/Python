"""
Lista de listas e seus indices
"""

salas = [
    # 0
    ['Elaine'], #0
    # 0        1
    ['Maria', 'Helena'], #1
    # 0       1       2
    ['Luiz', 'João', 'Eduardar', (0, 5, 10, 15, 20)] #2
]

print(salas) #Exibe tudo
print(salas[1]) #Exibe a lista inteira
print(salas[2][0]) #Exibe a lista com o referido indice da lista
print(salas[2][3][2]) #Exibe a lista com o referido indice da lista + indice da tupla

print('**********************')
for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)