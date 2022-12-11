n=int(input())
d=list(map(int,input().split()))
for i in d:
    if d.count(i)>n//2:
        a=i
print(a)