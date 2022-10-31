def prime(n):
    c=0
    for i in range(2,n//2):
        if n%i==0:
            c+=1
            return False
    return True
m=int(input())
n=int(input())
for i in range(m,n+1):
    if prime(i) and i!=1 and i!=4:
        print(i)