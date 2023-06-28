n,m = map(int,input().split())
mat = []
tc = bc = 0
for i in range(n):
    r = list(map(int,input().split()))
    mat.append(r)
    tc+=sum(r)
for i in range(n):
    for j in range(m):
        if i ==0 or j ==0 or i == n-1 or j == m-1:
            bc+=mat[i][j]
print(tc-bc)