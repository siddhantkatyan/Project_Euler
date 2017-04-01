
a,b,r,s = 3,7,0,1
for q in range(1000000,2,-1):
    p = (a*(q-1))/b;
    if (p*s>r*q):
        s,r = q,p
print r

