#!python3

# convert mixed numbers to improper fractions
# convert improper fractions to mixed numbers of type a + b/c

from math import floor


def toImproper(a,b,c):
    # a : whole number
    # b : numerator
    # c : denominator
    mult_num = a * c
    new_n = mult_num + b 
    frac = (new_n, c)
    return frac

def toMixed(num,den):
    #num: numerator
    #den: denominator
    # return a: whole number, b: numerator, c: denominator
    n_divided = num / den
    n_divided = floor(n_divided)
    new_n = num - (n_divided * den)
    frac = (n_divided, new_n, den)
    return frac

if __name__ == "__main__":
    assert toMixed(10,3) == (3,1,3)
    assert toMixed(3,4) == (0,3,4)
    assert toMixed(9,2) == (4,1,2)
    assert toImproper(5,1,3) == (16,3)
    assert toImproper(2,1,2) == (5,2)
