a = 'A'
b = 'B'
c = 1.1

string1 = 'a={0} b={1} c={2:.2f}'
formato1 = string1.format(a, b, c)

string2 = 'a={nome1} b={nome2} c={nome3:.2f}'
formato2 = string2.format(nome1=a, nome2=b, nome3=c)

print(formato1)
print(formato2)
