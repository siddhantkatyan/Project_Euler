print(sum({x*y for x in range(1,50) for y in range(100,2000) if ''.join(sorted(str(x)+str(y)+str(x*y))) == '123456789'}))
