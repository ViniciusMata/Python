"""
Fatiamento de string
 0 1 2 3 4 5 6 7 8
 O l á   M u n d o
-9-8-7-6-5-4-3-2-1
Fatiamento 
    [i:f:p] #i = inicio | f=fim | p=passo (pular)
    [::]  #Retorna a string inteira
Obs: a função LEN retorna a qtd de caracteres de uma str
"""

variavel = 'Olá Mundo'
print(variavel[1:8:2])
print(len(variavel))
print(variavel[::-1]) #escreve ao contrario a string OU variavel[-1:-10:-1] para o exemplo da str