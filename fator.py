"""
printa uma lista de fatores primos para um dado numero
ex.:
        In [1]: import fator

        In [2]: fator.fator(1256)
        Out[2]: [2, 2, 2, 157]

        In [3]: fator.primos[29]
        Out[3]: 113
"""
primos = []
parq = open("primo.txt",'r')
for line in parq:
    primos.append(int(line.split(',')[0]))
def fator(num):
    v = 0
    f = []
    while num!=1:
        p = primos[v]
        x = num/p
        if x*p==num:
            num=x
            f.append(p)
            v=0
        else:
            v+=1
    return f
