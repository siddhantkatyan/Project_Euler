e=[]
for i in range(999,100,-1):
    for j in range(i-1,100,-1):
        s = str(i*j)
        if s == s[::-1]:
            e.append(int(s))
            
            
print max(e)   
    
