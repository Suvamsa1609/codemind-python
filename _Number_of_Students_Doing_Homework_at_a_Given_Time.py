n=int(input())
d1=list(map(int,input().split()))
m=int(input())
d2=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n):
    for j in range(m):
        if i==j and d1[i]<=k and d2[j]>=k:
            c+=1
print(c)