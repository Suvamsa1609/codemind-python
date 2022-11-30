def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def palindrome(n):
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
n=int(input())
for i in range(n+1,99999):
    if prime(i) and palindrome(i):
        print(i)
        break