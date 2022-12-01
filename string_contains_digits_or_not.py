n=int(input())
for _ in range(n):
    s=input()
    for i in s:
        if i.isdigit():
            print("Yes")
            break
    else:
        print("No")