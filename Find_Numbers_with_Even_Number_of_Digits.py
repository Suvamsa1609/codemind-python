n=int(input())
d=list(map(str,input().split()))
c=0
for i in d:
    if len(i)%2==0:
        c+=1
print(c)