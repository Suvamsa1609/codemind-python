def fib(n):
    a=0
    b=1
    c=a+b
    while c<n:
        a=b
        b=c
        c=a+b
    return c
n=int(input())
if fib(n)==n:
    print("True")
else:
    print("False")