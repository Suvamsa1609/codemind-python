n = int(input())
lst = input().split()
d={}
for i in lst:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i]+=1
for k,v in d.items():
    if v == max(d.values()):
        print(k)