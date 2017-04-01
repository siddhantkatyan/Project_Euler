def generate_n_primes(N):
    primes  = []
    chkthis = 2
    while len(primes) < N:
        ptest = [chkthis for i in primes if chkthis%i == 0]
        primes += [] if ptest else [chkthis]
        chkthis += 1
    return primes
n = int(raw_input())
a = generate_n_primes(n)
print a[-1]
