def palindrome(n):
    temp=n
    rev=0
    while n:
        d=n%10
        rev=rev*10+d
        n=n//10
    if temp==rev:
        return True
    else:
        return False
n=int(input())
rc=c=0
for i in range(n-1,0,-1):
    rc+=1
    if palindrome(i):
        a=i
        break
for j in range(n+1,99999):
    c+=1
    if palindrome(j):
        b=j
        break
if rc>c:
    print(b)
elif rc<c:
    print(a)
else:
    print(a,b)