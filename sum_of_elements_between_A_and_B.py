n=int(input())
d=list(map(int,input().split()))
a,b=map(int,input().split())
sum=0
for i in range(n):
    if d[i]>=a and d[i]<=b:
        sum+=d[i]
print(sum)