import math
n=int(input())
d=list(map(int,input().split()))
sum=0
for i in d:
    ps=int(math.sqrt(i))
    if i==ps*ps:
        sum+=i
print(sum)