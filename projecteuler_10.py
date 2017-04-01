"""sieve of erasthones to find the first prime numbers, its complexity is n(log(n)"""

sieve = [True] * 200000000 # Sieve is faster for 2M primes
def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False
for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)
print sum(i for i in xrange(2, len(sieve)) if sieve[i]) 
