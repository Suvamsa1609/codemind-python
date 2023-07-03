s = input()
v='aeiouAEIOU'
d = []
for i in range(len(s)):
    if s[i] in v:
        if s[i] not in d:
            d.append(s[i])
if len(d):
    print(*d)
else:
    print("-1")