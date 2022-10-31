def neon(n):
    s=0
    while n:
        d=n%10
        n=n//10
        s=s+d
    return s
n=int(input())
sq=n*n
if neon(sq)==n:
    print("Neon Number")
else:
    print("Not Neon Number")