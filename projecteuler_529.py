


c = 0
for n in range(19,10**5):
    n = str(n)
    i =0
    while sum(map(int, n[i:]))>=10:
        sums = 0
        j = i
        while sums!=10:
            sums+=int(n[j])
            if sums>10:
                break
            j+=1
        if j==len(n):
            c+=1
            break
        i+=1   
        
print c
