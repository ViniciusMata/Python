"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (746824890)
   11  10  9   8   7   6   5   4   3   2
*  7   4   6   8   2   4   8   9   0   7   <-- PRIMEIRO DIGITO
   77  40  54  64  14  24  40  36  0   14

Somar todos os resultados: 
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
301 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for MAIOR que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpfEnviado = '74682489070'

noveDigitos = cpfEnviado[0:9]
contadorRegressivo_1 = 10
resultadoDigito_1 = 0

for digito_1 in noveDigitos:
    resultadoDigito_1 += int(digito_1) * contadorRegressivo_1
    contadorRegressivo_1 -= 1

digito_1 = (resultadoDigito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dezDigitos = + str(digito_1)
contadorRegressivo_2 = 11

resultadoDigito_2 = 0
for digito in dezDigitos:
    resultadoDigito_2 += int(digito) * contadorRegressivo_2
    contadorRegressivo_2 -= 1

digito_2 = (resultadoDigito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpfCalculo = f'{noveDigitos}{digito_1}{digito_2}'

if cpfEnviado == cpfCalculo:
    print(f'CPF {cpfEnviado} é VÁLIDO')
else:
    print(f'CPF {cpfEnviado} é INVÁLIDO')
