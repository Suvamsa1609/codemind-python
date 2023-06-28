n,m = map(int,input().split())
mat = []
for i in range(n):
    r = list(map(int,input().split()))
    mat.append(r)
c = 0
for i in range(n):
    if mat[i] == sorted(mat[i]) or mat[i] == sorted(mat[i],reverse = True):
        c+=1
print(c)