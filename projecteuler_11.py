n = 1000000
cache,cache[1],sl,sno = [None]*(n+1),1,0,0
for i in range(2,n):
    sq,k = i,0
    while sq!=1 and sq>=i:
        k+=1
        if sq%2==0:
            sq=sq/2
        else:
            sq=sq*3+1
    cache[i]=k+cache[sq]
    if cache[i]>sl:
        sl,sno=cache[i],i
print sno
        


