"""
CONSTANTE = 'Variaveis' que não vão mudar
Muitas condições no mesmo IF (ruim)
     <- Contagem de complexidade (ruim)
"""

velocidade = 65 #velocidade atual do carro
local_km_carro = 100 #local em que o carro está na estrada

RADAR_1 = 60 #velocidade máxiam do radar 1
LOCAL_1 = 100 #local onde está o radar 1
RADAR_RANGE = 1 #distância onde o radar pega

velocidade_carro_passou_radar1 = velocidade > RADAR_1
carro_passou_radar1 = local_km_carro >= (LOCAL_1 - RADAR_RANGE) and local_km_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = carro_passou_radar1 and velocidade_carro_passou_radar1

if velocidade_carro_passou_radar1:
    print(f'Velocidade carro passou no radar 1 = {velocidade} km/h')

if carro_passou_radar1:
    print('Carrou passou pelo radar 1')

if carro_multado_radar1:
    print('Carro foi multado no radar 1')