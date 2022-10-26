def prime(n):
    c=0
    for i in range(2,n//2):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
n=int(input())
for i in range(2,n//2):
    if n%i==0:
        j=n//i
        if prime(i) and prime(j):
            print(i,j)
            break
else:
    print("-1")