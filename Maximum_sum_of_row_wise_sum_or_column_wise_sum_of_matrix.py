n,m = map(int,input().split())
mat = []
d = []
for i in range(n):
    r = list(map(int,input().split()))
    mat.append(r)
for i in range(m):
    cs = 0
    for j in range(n):
        cs+=mat[j][i]
        d.append(cs)
for i in range(n):
    rs = 0
    for j in range(m):
        rs+=mat[i][j]
        d.append(rs)
print(max(d))