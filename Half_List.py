n=int(input())
d=list(map(int,input().split()))
a=[]
for i in range(n-1,n//2-1,-1):
    a.append(d[i])
for i in range(n//2):
    a.append(d[i])
print(*a)