n=int(input())
d=list(map(int,input().split()))
sum=0
for i in d:
    if i%2:
        break
    sum+=i
print(sum)