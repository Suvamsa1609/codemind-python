s = input()
v = 'aeiou'
max = 0
c = 0
for i in s:
    if i in v:
        c+=1
    if i not in v:
        c = 0
    if c > max:
        max = c
print(max)
    