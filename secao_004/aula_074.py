"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}'
    return saudar

s1 = criar_saudacao('Bom dia', 'Vinicius')
s2 = criar_saudacao('Bom tarde', 'Vinicius')
s3 = criar_saudacao('Bom noite', 'Vinicius')

print(s1())
print(s2())
print(s3())
