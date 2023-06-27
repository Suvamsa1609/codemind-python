n,m = map(int,input().split())
mat = []
d = []
for i in range(n):
    r = list(map(int,input().split()))
    mat.append(r)
for i in range(m):
    s = 0
    for j in range(n):
        s+=mat[j][i]
        d.append(s)
print(max(d))