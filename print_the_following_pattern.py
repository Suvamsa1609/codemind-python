def fun(n):
    for i in range(1,n+1):
        print(i,end="")
n=int(input())
for i in range(n):
    fun(n)
    print()
    n=n-1