n,k=map(int,input().split())
d=list(map(int,input().split()))
c=0
for i in d:
    if i%k==0:
        c+=1
print(c)