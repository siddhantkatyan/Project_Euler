

# list of generalized pentagonal numbers for generating function
k = sum([[i*(3*i - 1)/2, i*(3*i - 1)/2 + i] for i in range(1, 250)], [])

p, sgn, n, m  = [1], [1, 1, -1, -1], 0, 1e6

while p[n]>0:    # expand generating function to calculate p(n)
    n += 1
    px, i = 0, 0
    while k[i] <= n:
        px += p[n - k[i]] * sgn[i%4]
        i += 1
    p.append(px % m)

print "Project Euler 78 Solution =", n
