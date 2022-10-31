def Disarium(n):
    l=0
    while n:
        d=n%10
        n=n//10
        l+=1
    return l
n=int(input())
temp=n
l=Disarium(n)
s=0
while l:
    d=n%10
    s=s+d**l
    n=n//10
    l-=1
if s==temp:
    print("True")
else:
    print("False")
    