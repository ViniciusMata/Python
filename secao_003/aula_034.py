"""
Repetições
While (enqunato)
Executa uma ação enquanto uma condição for verdadeira
Loop Infinito = Quando um codigo nao tem fim
"""

condicao = True

while condicao:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome}')

    if nome == 'Sair':
        break