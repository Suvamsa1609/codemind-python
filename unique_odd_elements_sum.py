n=int(input())
d=list(map(int,input().split()))
a=[]
for i in d:
    if i not in a:
        a.append(i)
s=0
for i in a:
    if i%2:
        s+=i
print(s)