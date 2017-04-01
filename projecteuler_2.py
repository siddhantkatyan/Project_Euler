startNumber = int(raw_input("Enter the start number here "))
endNumber = int(raw_input("Enter the end number here "))

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

a = map(fib, range(startNumber, endNumber+2))
sums=0
for i in range(0,len(a)):
    if a[i]%2==0:
        sums = sums + a[i]

print sums
