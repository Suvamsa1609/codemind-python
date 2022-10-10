import math
def isprime(n):
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
def reverse(n):
    rev=0
    while n:
        d=n%10
        n=n//10
        rev=rev*10+d
    return rev
n=int(input())
if isprime(n):
    n=reverse(n)
    if isprime(n):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")