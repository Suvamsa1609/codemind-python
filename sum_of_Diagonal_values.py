n,m = map(int,input().split())
mat = []
for i in range(n):
    r = list(map(int,input().split()))
    mat.append(r)
n = len(mat)
s = 0
for i in range(n):
    s+=mat[i][i]
    s+=mat[i][n-1-i]
if n%2 != 0:
    s-=mat[n//2][n//2]
print(s)