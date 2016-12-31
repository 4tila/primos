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
