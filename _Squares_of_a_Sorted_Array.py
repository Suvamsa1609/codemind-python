n=int(input())
d=list(map(int,input().split()))
a=[]
for i in d:
    a.append(i*i)
print(*sorted(a))