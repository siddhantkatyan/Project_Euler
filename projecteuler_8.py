s = int(raw_input())
s = list(str(s))
n = 0
for i in range(0, len(s)-12):
    p = 1
    for j in range(i,i+13):
        p = p * int(s[j])
    if p > n: n = p
print n
