def palindrome(n):
    rev=0
    while n:
        d=n%10
        n=n//10
        rev=rev*10+d
    return rev
m=int(input())
n=int(input())
for i in range(m,n+1):
    if i==palindrome(i):
        print(i,end=" ")