def large(n):
    max=0
    while n:
        r=n%10
        if max<r:
            max=r
        n=n//10
    return max
n=int(input())
res=large(n)
print(res)