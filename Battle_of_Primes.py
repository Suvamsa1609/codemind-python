def prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n1=int(input())
n2=int(input())
sum=n1+n2
for i in range(sum+1,99999):
    if prime(i):
        break
print(i-sum)