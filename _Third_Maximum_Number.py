n=int(input())
d=list(map(int,input().split()))
a=[]
for i in d:
    if i not in a:
        a.append(i)
b=sorted(a)
if n>=3:
    print(b[len(b)-3])
else:
    print(max(d))