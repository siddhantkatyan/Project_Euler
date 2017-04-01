b = []
for i in range(1,1000000):
    t = i
    a = []
    while i>=1:
        if i%2==0:
            a.append('0')
        else:
            a.append('1')
        i=i/2
    if a[:]==a[::-1] and str(t)==str(t)[::-1]:
        b.append(t) 
print sum(b)

