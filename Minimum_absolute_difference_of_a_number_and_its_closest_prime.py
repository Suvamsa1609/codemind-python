def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
for i in range(n,999999):
    if prime(i):
        fd=abs(n-i)
        break
for j in range(n,0,-1):
    if prime(j):
        bd=n-j
        break
if fd<bd:
    print(fd)
else:
    print(bd)