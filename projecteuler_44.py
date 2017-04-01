'''def pe44():
    ps = set()
    i = 0
    while True:
        i += 1
        p = (3*i*i - i) / 2
        ps.add(p)
        for n in ps:
            if p-n in ps and p-2*n in ps: 
                return p-2*n
    
print "Project Euler 44 Solution =", pe44()
'''

def generate_pentagonals(x):
    for i in xrange(1, x+1):
        yield i * (3 * i - 1) / 2


def find_pentagonals():
    pentagonals = set(generate_pentagonals(2500))
    for x in pentagonals:
        for y in pentagonals:
            if x + y in pentagonals and x - y in pentagonals:
                return x - y

print find_pentagonals()
