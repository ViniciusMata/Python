"""
Gerador de CPF
"""

import random

noveDigitos = ''
for i in range(9):
    noveDigitos += str(random.randint(0, 9))

contadorRegressivo_1 = 10
resultadoDigito_1 = 0

for digito_1 in noveDigitos:
    resultadoDigito_1 += int(digito_1) * contadorRegressivo_1
    contadorRegressivo_1 -= 1

digito_1 = (resultadoDigito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dezDigitos = noveDigitos + str(digito_1)
contadorRegressivo_2 = 11

resultadoDigito_2 = 0
for digito in dezDigitos:
    resultadoDigito_2 += int(digito) * contadorRegressivo_2
    contadorRegressivo_2 -= 1

digito_2 = (resultadoDigito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpfCalculo = f'{noveDigitos}{digito_1}{digito_2}'

print(f'Novo CPF gerado: {cpfCalculo}')
