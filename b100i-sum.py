#!python3

# program to add 2 fractions
# return the sum of the 2 fractions as a tuple with numerator and
# denominator in lowest terms
from a100ilowestterms import lowestTerms

def sum(n1,d1,n2,d2):
    if d1 == d2:
        #addedpair = (n1+n2, d1)
        added_n = n1+n2
        lowestadded = lowestTerms(added_n, d1)
        return lowestadded
    else:
        n1_x = n1 * d2
        d1_x = d1 * d2
        n2_x = n2 * d1
        d2_x = d1 * d2
        #addedpair = [n1_x+n2_x, d2_x]
        added_n = n1_x + n2_x
        added_d = d2_x
        lowestadded = lowestTerms(added_n, added_d)
        #print (lowestadded)
        return lowestadded

if __name__ == "__main__":
    assert sum(1,3,2,1) == (7,3)
    assert sum(1,4,3,4) == (1,1)
    assert sum(5,2,3,5) == (31,10)
