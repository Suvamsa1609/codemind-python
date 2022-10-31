def happy(n):
    s=0
    while n:
        d=n%10
        n=n//10
        s=s+d**2
    return s
n=int(input())
while n>=9:
    n=happy(n)
if n==1 or n==7:
    print("True")
else:
    print("False")