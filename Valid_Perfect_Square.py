def per_sq(n):
    for i in range(n//2+1):
        if i*i==n:
            return True
    return False
t=int(input())
for _ in range(t):
    n=int(input())
    print(per_sq(n))