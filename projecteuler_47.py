import time
def primes(n):
    primfac,d = [],2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac
i,c,b = 210,0,[]
while c!=4:
    f = primes(i)
    if len(set(f))==4:
        b.append(i)
        c+=1
    else:
        del b[:]
        c=0
    i+=1
print b


start_time = time.time()

print("--- %s seconds ---" % (time.time() - start_time))

