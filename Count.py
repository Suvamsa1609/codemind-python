n=int(input())
d=list(map(int,input().split()))
ec=oc=0
for i in d:
    if i%2:
        oc+=1
    else:
        ec+=1
print(ec,oc)