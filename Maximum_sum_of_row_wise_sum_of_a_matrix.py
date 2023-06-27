n,m = map(int,input().split())
d = []
for i in range(n):
    s = 0
    r = list(map(int,input().split()))
    s+=sum(r)
    d.append(s)
print(max(d))