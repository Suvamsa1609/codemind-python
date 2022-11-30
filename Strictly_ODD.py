n=int(input())
d=list(map(int,input().split()))
c=oc=0
for i in range(n):
    if i%2 and d[i]%2:
        c+=1
    if d[i]%2:
        oc+=1
if c==oc:
    print(True)
else:
    print(False)