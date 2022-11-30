n=int(input())
d=list(map(int,input().split()))
a=[]
for i in d:
    if i not in a:
        a.append(i)
print(*a)