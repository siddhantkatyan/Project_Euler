import math
n = int(raw_input())
a = []
for num in range(2,n):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       a = a + [num]
sum = 1
for i in range(0,len(a)):
    k = a[i]
    m = 1
    c = k
    while c<=n:
        m+=1
        c = math.pow(k,m)
    t = math.pow(a[i], m-1)
    sum = sum * int(t)    
print sum        
