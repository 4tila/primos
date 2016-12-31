m = 2
print 2
print '     1'
def primo(num):
    v = False
    yn = ""
    k = 0
    i = 1
    try:
        while (num-1)/(num-i) !=0:
            if (num-1)/(num-i)==(num-1.0)/(num-i):
                if (m%num)**((num-1)/(num-i))%num==1:
                    v = True
                    yn = 'y'
                    k = (num-1)/(num-i)
                    break
            i+=1
    except ZeroDivisionError:
        k =  0
    if v==False:
        yn = "n"
    return (yn, k)
i = 3
print "running..."
while True:
    try:
        req = primo(i)
        if req[0]=='y':
            m*=i
            print i
            print "     "+str(req[1])
        else:
            pass
        i+=1
    except KeyboardInterrupt:
        break
