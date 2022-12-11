n=int(input())
d=list(map(int,input().split()))
k=int(input())
for i in d:
    if i+k>=max(d):
        print(True,end=" ")
    else:
        print(False,end=" ")