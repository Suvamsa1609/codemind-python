def rev(n):
    s=0
    while n:
       d=n%10
       s+=d
       n=n//10
    return s
n=int(input())
d=list(map(int,input().split()))
sum=0
for i in d:
    sum+=rev(i)
print(sum)