n=int(input())
d=list(map(int,input().split()))
fh=sh=0
for i in range(n//2):
    fh+=d[i]
for i in range(n//2,n):
    sh+=d[i]
print(sh-fh)