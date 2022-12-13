n=int(input())
d1=list(map(int,input().split()))
d2=list(map(int,input().split()))
z=list(zip(d1,d2))
for i in z:
    print(sum(i),end=' ')