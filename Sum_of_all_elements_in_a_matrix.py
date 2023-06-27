n,m = map(int,input().split())
mat = []
s = 0
for i in range(n):
    r = list(map(int,input().split()))
    mat.append(r)
    s+=sum(r)
print(s)