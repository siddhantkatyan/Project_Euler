dates = {'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
sums,c = 7,0
for i in range(1900,2000):
    j = 1
    if i%4==0 and ( i%100!=0 or i%400==0 ):
        dates['2']=29 
    while j<=12:
        sums+= 28
        sums = sums-dates[str(j)]
        if sums==1:
            sums+=7
            c+=1
        if sums<=0:
            sums+=7
        j+=1
print c
