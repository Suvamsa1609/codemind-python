n=int(input())
d=list(map(int,input().split()))
a=[]
for i in d:
    if i not in a:
        a.append(i)
c=0
for i in a:
    if i%2==0:
        c+=1
print(c)