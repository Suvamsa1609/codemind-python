def add_digits(n):
    sum=0
    while n:
        d=n%10
        n=n//10
        sum=sum+d
    return sum
n=int(input())
while n>9:
    n=add_digits(n)
print(n)