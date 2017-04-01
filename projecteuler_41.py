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

b = sieveOfAtkin(1000)
for i in range(7654321,0,-1):
    a = list(str(i))
    if len(set(a))==7 and  ('9' not in set(a)) and ('0' not in set(a)) and ('8' not in set(a)) :
        c = 0
        for j in range(0,len(b)):
            if i%b[j]==0:
                c+=1
                break
        if c==0:
            print i
            break
