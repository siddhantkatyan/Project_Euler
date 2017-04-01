a = []
b = []
s = 0
for i in range(2,355000):
   a = map(int,str(i))
   sq = [x**5 for x in a]
   if sum(sq)==i:
       b.append(i)
       
print sum(b)
