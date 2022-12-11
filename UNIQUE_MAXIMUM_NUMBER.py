n=int(input())
d=list(map(int,input().split()))
a=[]
flag=0
for i in d:
    if d.count(i)==1:
        a.append(i)
        flag=1
if flag==0:
    print("-1")
else:
    print(max(a))