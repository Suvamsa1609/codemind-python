s = input().split()
for i in range(len(s)):
    if i%2 == 0:
        print(s[i][::-1],end= ' ')
    if i%2:
        print(s[i],end= ' ')