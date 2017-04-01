from math import factorial

sums=0
for i in range(100,200):
    a = (map(int, str(i)))
    for j in range(0,len(a)):
         sums = sums + factorial(a[j])
    if sums == i:
         print i


