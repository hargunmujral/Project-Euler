import math

def isPrime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False 
    square_root = int(math.sqrt(n))
    for i in range(3, square_root+1, 2) :
        if n % i == 0:
            return False 
    return True

def nthPrime(n):
    count = 1
    i = 1
    while count < n:
        i += 2
        if isPrime(i):
            count += 1
    return i

print(nthPrime(1))
print(nthPrime(2))
print(nthPrime(3))
print(nthPrime(4))
print(nthPrime(5))
print(nthPrime(6))
print(nthPrime(10001))
