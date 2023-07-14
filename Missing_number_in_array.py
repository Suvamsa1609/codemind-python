t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int,input().split()))
    ans = 0
    for i in range(1,n+1):
        ans = ans^i
    for i in c:
        ans = ans^i
    print(ans)