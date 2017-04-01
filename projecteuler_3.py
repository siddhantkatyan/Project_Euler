import math
n = int(raw_input())
def primes(a):
    c = 0
    sqr = math.sqrt(a)
    sqr = math.ceil(sqr)
    sqr = int(sqr)
    for i in range(2,sqr):
        if a%i==0:
            c+=1
    if c==0:
        return 1
sq = int(math.sqrt(n))
for i in range(2,sq):
    if n%i==0 and primes(i)==1:
        print i
