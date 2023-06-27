n = int(input())
mat1 = []
mat2 = []
mat = []
for i in range(n):
    r1 = list(map(int,input().split()))
    mat1.append(r1)
for i in range(n):
    r2 = list(map(int,input().split()))
    mat2.append(r2)
for i in range(n):
    for j in range(n):
        print(mat1[i][j]+mat2[i][j],end=" ")
    print()