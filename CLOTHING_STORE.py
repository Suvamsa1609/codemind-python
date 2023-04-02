n = int(input())
lst = input().split()
d={}
for i in lst:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
c=0
for v in d.values():
    c = c + (v//2)
print(c)