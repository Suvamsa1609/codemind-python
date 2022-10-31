def palindrome(n):
    rev=0
    while n:
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev
t=int(input())
for _ in range(t):
    n=int(input())
    if palindrome(n)==n:
        print("True")
    else:
        print("False")