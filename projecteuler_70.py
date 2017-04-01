import timeit
import math
start = timeit.default_timer()
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

a = sieveOfAtkin(4000)
nm=5
for i in a[::-1]:
      for j in a[::-1]:
            if i*j < 10000000 and sorted(str(i*j)) == sorted(str((i-1)*(j-1))):
                  n = i*j/(i-1)/(j-1)
                  if n < nm:
                        nm = n
                        print(i*j)
                  break


stop = timeit.default_timer()
print stop - start

