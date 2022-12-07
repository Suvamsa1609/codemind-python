n=int(input())
d=list(map(int,input().split()))
sum=flag=0
a=[]
for i in d:
    if i==d.count(i) and i not in a:
        a.append(i)
print(len(a))