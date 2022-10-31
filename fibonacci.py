n=int(input())
a=0
b=1
c=a+b
print(a,b,c,end=" ")
i=3
while i<n:
    a=b
    b=c
    c=a+b
    print(c,end=" ")
    i+=1