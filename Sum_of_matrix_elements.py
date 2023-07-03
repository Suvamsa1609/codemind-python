m = int(input())
n = int(input())
mat=[]
s = 0
for i in range(m):
    r = list(map(int,input().split()))
    mat.append(r)
s = 0
for i in range(m):
    for j in range(n):
        s+=mat[i][j]
print(s)