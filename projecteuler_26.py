from decimal import *
getcontext().prec = 10000
i = 1
while i!=100:
    n = Decimal(1/float(i))
    dec = str(n-int(n))[1:]
    print (dec[1:])
    i+=1

