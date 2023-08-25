import math
def gcd(a,b):
    return math.gcd(a,b)
n = int(input())
arr = list(map(int,input().split()))
res = 0
for i in range(n):
    res = gcd(res,arr[i])
print(res)