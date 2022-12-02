def count(n):
    c=0
    while n:
        d=n%10
        c+=1
        n=n//10
    print(c,end=" ")
n=int(input())
d=list(map(int,input().split()))
for i in d:
    if i>0:
        count(i)
    elif i<0:
        i=abs(i)
        count(i)
    else:
        print("1",end=" ")