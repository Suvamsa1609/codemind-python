def pretty(l,r):
    count=0
    for i in range(l,r+1):
        d=i%10
        if d==2 or d==3 or d==9:
            count+=1
    return count
t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    print(pretty(l,r))