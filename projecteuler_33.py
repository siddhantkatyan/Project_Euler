denproduct = 1;
nomproduct = 1;
for i in range(1,10):
    for den in range(1,i):
        for nom in range(1,den):
            if ((nom * 10 + i) * den == nom * (i * 10 + den)):
                denproduct *= den;
                nomproduct *= nom;    
print denproduct
print nomproduct
