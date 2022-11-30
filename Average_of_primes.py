def prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input())
d=list(map(int,input().split()))
c=s=0
for i in d:
    if prime(i):
        c+=1
        s+=i
        avg=s/c
print("%.2f"%avg)