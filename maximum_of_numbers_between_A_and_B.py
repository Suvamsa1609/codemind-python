n=int(input())
d=list(map(int,input().split()))
a,b=map(int,input().split())
flag=0
max=0
for i in range(n):
    if d[i]>=a and d[i]<=b:
        if d[i]>max:
            max=d[i]
            flag=1
if flag==0:
    print("-1")
else:
    print(max)