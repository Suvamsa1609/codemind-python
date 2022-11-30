n=int(input())
d=list(map(int,input().split()))
k=int(input())
sum=0
for i in d:
    sum+=i
    if i==k:
        break
print(sum)