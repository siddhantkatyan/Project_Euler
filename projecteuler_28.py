j,i,sums = 3,1,0
while i<=(j**2) and j<=1001:
    sums+=i
    i+=(j-1)
    if i!=j**2:
        continue
    else:
        j+=2
print sums+i       
        
    
    



    
