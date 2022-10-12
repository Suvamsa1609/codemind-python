def digitcount(n):
    c=0
    ec=0
    oc=0
    while n:
        d=n%10
        n=n//10
        c+=1
        if d%2==0:
            ec+=1
        else:
            oc+=1
    if c==ec:
        return "Even"
    elif c==oc:
        return "Odd"
    else:
        return "Mixed"
n=int(input())
dc=digitcount(n)
print(dc)