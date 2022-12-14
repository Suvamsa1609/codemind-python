def count(n):
    rev=c=0
    while n:
        d=n%10
        rev=rev*10+d
        c+=1
        n=n//10
    return c
n=int(input())
d=list(map(int,input().split()))
min=99999999
a=[]
for i in d:
    if count(i)<min:
        min=count(i)
for i in d:
    if count(i)==min:
        a.append(i)
print(len(a))