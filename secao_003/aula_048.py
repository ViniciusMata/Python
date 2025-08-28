"""
Lista em Python
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - índices e fatiamento
Métodos úteis: 
    append -> adiciona um item ao final
    insert -> adiciona um item no indice escolhido
    pop -> Remove do final OU do indice escolhido
    del -> apaga um indice escolhido
    clear -> limpa a lista
    extend -> estenda a lista
    + -> Concatena listas
Create, Read, Update,   Delete     = lista[i] (CRUD)
Criara, Ler, Atualizar, Deletar    = lista[i] (CRUD)


#        +01234
#        -54321
#string = 'ABCDE' #5 Caracteres
#print(bool([])) #False
#print(lista, type(lista))

#        0    1      2          3     4
#       -5   -4     -3         -2    -1
lista = [123, True, 'Vinicius', 12.3, []]
print(lista[2], type(lista[2]))

print()

#Create
lista.append('Teste')
print('Create => ', lista)

#Read
leitura = lista[2]
print('Read => ', leitura) #or print(lista[2])

#Update
lista[2] = 'Vinicius Mata'
print('Update => ', lista[2])

#Delete
del lista[3]
print('Delete => ', lista)

#Pop = Remove sempre o ultimo item da lista OU o indice passado
lista.pop() #Or lista.pop(3) -> Passa o indice
print(lista) 

#Clear = Lipmar lista
lista.clear()
print(lista)

#Insert = incluir a lista em um indice que queira
lista = [123, True, 'Vinicius', 12.3, []]
lista.insert(0, 'Teste') #1º = Indice | 2º = Valor
print(lista)

print()

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)

#Extend = Adiciona os valores no parametro informado antes do metodo .extend
lista_a.extend(lista_b)
print(lista_a)

"""




"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Vinicius', 'Stephanie', 'Lucas']
lista_b = lista_a.copy()

lista_a[0] = 'Quem é ?'
print(lista_a)
print(lista_b)