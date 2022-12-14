def count(n):
    c=0
    if n<0:
        n=abs(n)
    if n==0:
        return 1
    while n>0:
        d=n%10
        c+=1
        n=n//10
    return c
n,k=map(int,input().split())
d=list(map(int,input().split()))
c=0
for i in d:
    if count(i)==k:
        c+=1
print(c)