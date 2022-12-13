#x+=rev(x)
#if x==pal(x)
def pal(n):
    temp=n
    rev=0
    while n:
        d=n%10
        rev=rev*10+d
        n=n//10
    if temp==rev:
        return True
    else:
        return False
def reverse(n):
    r=0
    while n:
        d=n%10
        r=r*10+d
        n=n//10
    return r
x=int(input())
while True:
    x=x+reverse(x)
    if pal(x):
        print(x)
        break