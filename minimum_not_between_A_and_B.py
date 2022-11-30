n=int(input())
d=list(map(int,input().split()))
a,b=map(int,input().split())
flag=0
min=999
for i in range(n):
    if d[i]<a or d[i]>b:
        if d[i]<min:
            min=d[i]
            flag=1
if flag==0:
    print("-1")
else:
    print(min)