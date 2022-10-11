a,b=map(int,input().split())
n=a
if b==n+1 or b==n-1:
    print("Yes")
elif n==1 and b==10 or n==10 and b==1:
    print("Yes")
else:
    print("No")