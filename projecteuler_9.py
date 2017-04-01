for num in range(1, 1000):
    for dig in range(num, 1000 - num):
        i = 1000 - num - dig
        if num * dig + 1000 * i == 500000:
            print num, dig, i
            print num*dig*i

"""
(num+dig+i)^2=1000^2

Expand:
num2+dig2+i2+2numdig+2numi+2digi=1000000
num2+dig2+i2+2numdig+2numi+2digi=1000000
Use triplet equality:
2i2+2numdig+2numi+2digi=1000000
2i2+2numdig+2numi+2digi=1000000
Factor:

i(num+dig+i)+numdig=500000
i(num+dig+i)+numdig=500000
Use fact that num+dig+i=1000num+dig+i=1000 in our case:

numdig+1000i=500000
"""
