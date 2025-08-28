"""
Exercicio
Peço ao usuario para digitar seu nome +  idade
Se nome e didade forem digitados:
    Exiba:
        Seu nome
        Seu nome invertido
        Seu nome contém (ou não) espaços
        Seu nome tem 'x' letras
        A primeira letra do nome
        A ultima letra do nome
Se nada for digitado em nome e idade:
    Exiba:
        "Desculpe, você deixou campos vazios.
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra é {nome[0]}')
    print(f'A última letra é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')
