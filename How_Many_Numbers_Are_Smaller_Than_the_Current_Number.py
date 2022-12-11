n=int(input())
d=list(map(int,input().split()))
a=[]
for i in d:
    c=0
    for j in d:
        if j<i:
            c+=1
    a.append(c)
print(*a)