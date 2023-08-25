def gcd(a,b):
    while a>0 and b>0:
        if a>b:
            a = a%b
        else:
            b = b%a
    if a == 0:
        return b
    return a
def gcd_n(arr):
    res = 0
    for i in range(n):
        res = gcd(res,arr[i])
    return res
n = int(input())
arr = list(map(int,input().split()))
print(gcd_n(arr))