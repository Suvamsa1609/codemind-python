n=int(input())
d=list(map(int,input().split()))
sum=0
m=n-1
for i in range(n):
    sum+=d[i]*(2**m)
    m-=1
print(sum)