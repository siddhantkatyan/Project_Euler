import math
def sieveOfAtkin(limit):
    P = [2,3]
    sieve=[False]*(limit+1)
    for x in range(1,int(math.sqrt(limit))+1):
        for y in range(1,int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7 : sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p] : P.append(p)
    return P
b = sieveOfAtkin(1000000)
t = 0
m = 0
for i in range(5,len(b)):
    a = list(str(b[i]))
    c = 1
    f = len(a)-1
    while c<=len(a)-1:
        d = ''.join(a[c:])
        e = ''.join(a[0:f])
        if int(d) in b and int(e) in b:
            c+=1
            f-=1
            continue
        else:
            break
    if c==len(a) and f==0:
        t+=1
        m+= b[i]
    if t==11:
        print m
        break
    
