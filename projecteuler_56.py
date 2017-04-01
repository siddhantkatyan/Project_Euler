max_sd, max_a, max_b = 0, 0, 0

for a in range(90, 100):
    for b in range(90, 100):
        sum_digits = sum(int(digit) for digit in str(a**b))
        if sum_digits > max_sd: max_sd, max_a, max_b = sum_digits, a, b

print "Project Euler 56 Solution =", max_sd, "a=", max_a, "b=", max_b
