import math
def perfectsquare(n):
    sq=int(math.sqrt(n))
    if sq*sq==n:
        return True
    else:
        return False
n=int(input())
print(perfectsquare(n))