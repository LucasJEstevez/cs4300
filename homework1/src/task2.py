# int1 ^ int2 (will round as this uses integers)
def task2_exponent_integers(int1,int2):
    int1 = int(int1)
    int2 = int(int2)
    return int1**int2

#flt1^flt2 (will not round, uses floats)
def task2_exponent_floats(flt1,flt2):
    return round(flt1**flt2,2)

#concatenates items together, even non-strings
def task2_concat(str1,str2):
    return str(str1)+str(str2)

#Returns flt1 % flt2
def task2_mod(flt1,flt2):
    return round(flt1%flt2,2)
