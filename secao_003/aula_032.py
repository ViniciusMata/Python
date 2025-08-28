"""
Faça um programa que peça ao usuario para digitar um numero inteiro.
Informe se este numero é par ou impar. Caso o usuario não digite um numero inteiro,
Informe que não é um numero inteiro.

numero = input('digite um numero: ')

try:
    numeroInt = int(numero)
    if (numeroInt % 2) == 0:
        print(f'Numero {numeroInt} é PAR')
    else:
        print(f'Numero {numeroInt} é ÍMPAR')
except:
    print('Você não digitou um numero inteiro')

"""


"""
Faça um programa que pergunta a hora ao usuário e baseando-se no horário descrito, exiba a saudação apropriada
Ex.: Bom dia (00-11), Boa tarde (12-17), Boa Noite (18-23)

hora = input('Digite a hora: ')

try:
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite')
    else:
        print('Informe um hora válida')
except:
    print('Digite apenas um numero inteiro')

"""


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto".
Se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu nome: ')

nome_str = str(nome)
tam_nome = len(nome_str)
if tam_nome > 0:
    if tam_nome <= 4:
        print('Seu nome é curto')
    elif tam_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')
