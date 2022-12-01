def palindrome(s):
    a=s[::-1]
    if s==a:
        return True
    else:
        return False
t=int(input())
for _ in range(t):
    s=input()
    if palindrome(s):
        if len(s)%2:
            print("YES ODD")
        else:
            print("YES EVEN")
    else:
        print("NO")