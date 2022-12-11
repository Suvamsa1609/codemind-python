n=int(input())
d=list(map(int,input().split()))
a=[]
for i in d:
    if i!=0:
        a.append(i)
for i in d:
    if i==0:
        a.append(i)
print(*a)