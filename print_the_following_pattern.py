def fun(n):
    for i in range(n,0,-1):
        print(i,end=" ")
        i-=1
n=int(input())
for i in range(n):
    fun(n)
    print()