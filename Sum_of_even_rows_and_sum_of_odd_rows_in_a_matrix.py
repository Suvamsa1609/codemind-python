n,m = map(int,input().split())
mat = []
es = os = 0
for i in range(n):
    r = list(map(int,input().split()))
    mat.append(r)
    if i%2 == 0:
        es+=sum(r)
    else:
        os+=sum(r)
print(es,os)