n=int(input())
d=list(map(int,input().split()))
c=ec=0
for i in range(n):
    if i%2==0 and d[i]%2==0:
        c+=1
    if d[i]%2==0:
        ec+=1
if c==ec:
    print(True)
else:
    print(False)