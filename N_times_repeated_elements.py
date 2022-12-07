n=int(input())
d=list(map(int,input().split()))
k=int(input())
sum=flag=0
a=[]
for i in d:
    if d.count(i)==k and i not in a:
        a.append(i)
        flag=1
if flag==0:
    print("-1")
else:
    print(*a)