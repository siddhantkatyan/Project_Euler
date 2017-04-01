#Project Euler Problem 63

from math import log10

s = 0
for n in range(1, 10):
    s += int(1 / (1 - log10(n)))

print "n-digit integers that are an nth power =", s
