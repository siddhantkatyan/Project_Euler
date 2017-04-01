

c = 0
for i in range(11,1000000):
    s = list(str(i))
    sums = 0
    while sums!=89:
        sums = 0
        for j in range(0,len(s)):
            sums+=int(s[j])*int(s[j])
        del s
        s = list(str(sums))
        if sums == 1:
            break
        if sums == 89:
            c+=1
            break
        
print c  
