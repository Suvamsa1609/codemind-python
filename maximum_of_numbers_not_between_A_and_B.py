n=int(input())
d=list(map(int,input().split()))
a,b=map(int,input().split())
max=flag=0
for i in range(n):
    if d[i]<a or d[i]>b:
        if max<d[i]:
            max=d[i]
            flag=1
if flag==0:
    print("-1")
else:
    print(max)