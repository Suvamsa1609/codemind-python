def palindrome(n):
    temp=n
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    if temp==rev:
        return True
    else:
        return False
n=int(input())
d=list(map(int,input().split()))
c=0
for i in d:
    if palindrome(i):
        c+=1
print(c)
    