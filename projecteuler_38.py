e = []
for i in range(9234,9387):
    b = str(i)+str(i*2)
    if len(set(b))==9 and '0' not in b: e.append(b)
print max(e)
