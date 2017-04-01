import urllib2
pairs = urllib2.urlopen(file_url).read().split('\n')
mv, ml = 0, 0 
for ln, line in enumerate(pairs, start=1):
    b, e = line.split(',') 
    v = int(e) * log(int(b)) 
    if v > mv: 
        mv, ml = v, ln 
print "Project Euler 99 Solution =", ml
