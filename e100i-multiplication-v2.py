#!python3

# Duplicate of d100i-multiplication.py
# except this should accept mixed numbers:

from c100imixednumbers import toImproper
x = 0
y = 0
def product(f1,f2):
    # f1: tuple representing first fraction
        # a tuple with length 2 is a numerator/denominator 
        # a tuple with length 3 is a whole number/numerator/denominator
    # f2 is the same as 1
    x = 0
    y = 0
    f1_len = len(f1)
    f2_len = len(f2)
    if f1_len == 3:
        a = f1[0]
        b = f1[1]
        c = f1[2]
        new_f1 = toImproper(a, b, c)
        x = 1
    if f2_len == 3:
        a = f2[0]
        b = f2[1]
        c = f2[2]
        new_f2 = toImproper(a, b, c)
        y = 1
    if x == 1 and y != 1:
    
        d1 = new_f1[1] * f2[1]
        n1 = new_f1[0] * f2[0]
        frac = (n1, d1)
        return frac
    if x != 1 and y == 1:
    
        d1 = f1[1] * new_f2[1]
        n1 = f1[0] * new_f2[0]
        frac = (n1, d1)
        return frac
    if x == 1 and y == 1:
    
        d1 = new_f1[1] * new_f2[1]
        n1 = new_f1[0] * new_f2[0]
        frac = (n1, d1)
        return frac
    else:
        n1 = f1[0] * f2[0]
        d1 = f1[1] * f2[1]
        frac = (n1, d1)
        return frac
 
if __name__ == "__main__":
    assert product((1,3),(4,1,2)) == (9,6)
    assert product( (3,4) , (5,3) ) == (15,12)
    assert product( (3,1,2) , (2,1,2) ) == (35,4)