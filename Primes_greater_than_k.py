def prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input())
d=list(map(int,input().split()))
k=int(input())
c=0
for i in d:
    if i>=k and prime(i):
        c+=1
print(c)