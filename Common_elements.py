n,m=map(int,input().split())
d1=list(map(int,input().split()))
d2=list(map(int,input().split()))
a=[]
for i in d1:
    for j in d2:
        if i==j and j not in a:
            a.append(j)
print(*a)