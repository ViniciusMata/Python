"""
https://docs.python.org/pt-br/3/library/
Imutáveis que vimos: str, int, float, bool
"""

string1 = 'vinicius mata'
print(string1)
string2 = f'{string1[:7]}Z{string1[8:]}'
print(string2)

print(string2.capitalize())
print(string2.zfill(20))