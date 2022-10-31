def fun(n):
    s=0
    p=1
    while n:
        d=n%10
        n=n//10
        s+=d
        p*=d
    return p-s
n=int(input())
print(fun(n))