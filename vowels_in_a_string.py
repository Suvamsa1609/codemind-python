s = input()
v = input()
for i in range(len(s)):
    if v == s[i]:
        print(True)
        print(i)
        break
else:
    print(False)