i = 10**6
n = 10**15
a = []
sums = 31054319
while i<=n:
    sums +=sum(map(int, str(sums)))
    a.append(sums)
    i+=1
    print a[:-1]


