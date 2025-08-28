"""
Operadores logicos
and (e) or (ou) not (não)
and - tds as condicoes precisam ser verdadeiras
Se qql valor for falso, a expressao inteira sera avaliada naquele valor
Sao consideradas false
int=0 float=0.0 str='' bool=False
tbm existe o tipo none que é usado para representar um não valor
"""

entrada = input('[E]ntrar [S]air:' )
senha_digitada = input('Senha: ')

senha_permitida = '123'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

#Avaliacao de curto circuito
print(True or False or False)