import math
def isprime(n):
    sq=int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n=int(input())
if isprime(n):
    while n:
        d=n%10
        n=n//10
        if d==1 or d==4 or d==6 or d==9:
            print("Not Mega Prime")
            break
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")