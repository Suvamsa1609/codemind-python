n=int(input())
d=list(map(int,input().split()))
if n%2:
    print(*d,end=" 0")
else:
    print(*d)