import math
def isprime(n):
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return "not a prime"
    return "prime"
n=int(input())
print(isprime(n))