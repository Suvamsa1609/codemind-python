n=int(input())
d=list(map(int,input().split()))
sum=flag=0
a=[]
for i in d:
    if i==d.count(i):
        if i not in a:
            sum+=i
            a.append(i)
            flag=1
if flag==1:
    print("%.2f"%(sum/len(a)))
else:
    print("-1")