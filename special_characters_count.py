s = input().lower()
v = 'abcdefghijklmnopqrstuvwxyz0123456789 '
c = 0
for i in s:
    if i not in v:
        c+=1
print(c)