n=int(input())
d=list(map(int,input().split()))
a,b=map(int,input().split())
flag=0
for i in range(n):
    if d[i]<a or d[i]>b:
        print(d[i],end=" ")
        flag=1
if flag==0:
    print("-1")