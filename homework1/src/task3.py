import math

def task3_check_sign(num):
    if num > 0: return 'positive'
    elif num == 0: return 'zero'
    else: return 'negative'

def isPrime(num):
    if num < 2: return False
    else:
        for i in range(2,math.floor(math.sqrt(num))+1):
            if num%i == 0: return False
        return True

def task3_ten_primes():
    primes = []
    counter = 0
    num = 2
    while counter < 10:
        if isPrime(num):
            primes.append(num)
            counter += 1
        num+=1
    print(primes)

#def task3_product(num):
#    #Forces integer
#    if num%1 != 0:
#        num=int(num)
#    if num < 0: return -1
#    elif num == 0 or num == 1: return num
#    else:
#        prod = 1
#        for i in range(2,num):
#            prod*=i
#        return prod