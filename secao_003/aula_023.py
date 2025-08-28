"""
Operadores logicos "not"
Usado para inverter expressao
not True = False
not False = True
"""

senha_digitada = input('Senha: ')

senha_permitida = '123'

if not senha_digitada:
    print('Senha não Informada')
