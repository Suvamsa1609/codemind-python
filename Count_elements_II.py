n,m=map(int,input().split())
d1=list(map(int,input().split()))
d2=list(map(int,input().split()))
a=[]
c=s=0
for i in d1:
    if i not in d2 and i not in a:
        a.append(i)
        c+=1
for j in d2:
    if j not in d1 and j not in a:
        a.append(j)
        s+=1
print(c+s)