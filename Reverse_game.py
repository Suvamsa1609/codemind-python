def reverse(n):
    rev=0
    while n:
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev
n=int(input())
d=list(map(int,input().split()))
for i in d:
    print(reverse(i),end=" ")