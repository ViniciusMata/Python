"""
Repetições
While (enqunato)
Executa uma ação enquanto uma condição for verdadeira
Loop Infinito = Quando um codigo nao tem fim
"""

c = 0

while c <= 100:
    c += 1

    if c == 6:
        print('Nao vou mostrar o 6')
        continue

    if c >= 10 and c <= 27:
        print(f'Nao vou mostrar o {c}')
        continue

    print(c)

    if c == 40:
        break

print('Acabou')