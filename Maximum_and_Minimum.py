n=int(input())
d=list(map(int,input().split()))
sum=flag=0
a=[]
for i in d:
    if i==d.count(i) and i not in a:
        a.append(i)
        flag=1
if flag==0:
    print("-1")
else:
    print(min(a),max(a))