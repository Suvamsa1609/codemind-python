def phn(n):
    c=0
    while n:
        d=n%10
        n=n//10
        c+=1
    if c==10:
        return "Valid"
    else:
        return "Invalid"
n=int(input())
print(phn(n))