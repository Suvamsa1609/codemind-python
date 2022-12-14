def count(n):
    count=0
    if n<0:
        n=abs(n)
    while n:
        d=n%10
        count+=1
        n=n//10
    return count
n=int(input())
d=list(map(int,input().split()))
max=0
a=[]
for i in d:
    if count(i)>max:
        max=count(i)
for i in d:
    if count(i)==max:
        a.append(i)
print(*a)