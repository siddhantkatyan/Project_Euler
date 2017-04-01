def all_perms(str):
    if len(str) <=1 :
        yield str
    else:
        for perm in all_perms(str[1:]) :
            for i in range(len(perm)+1) :
                yield perm[:i] + str[0:1] + perm[i:]

totalsum = 0
for perm in all_perms("0123456789") :
    if int(perm[1:4]) % 2 \
    or int(perm[2:5]) % 3 \
    or int(perm[3:6]) % 5 \
    or int(perm[4:7]) % 7 \
    or int(perm[5:8]) % 11 \
    or int(perm[6:9]) % 13 \
    or int(perm[7:10]) % 17 :
        continue
    
    totalsum += int(perm)
    print perm
    
print totalsum
