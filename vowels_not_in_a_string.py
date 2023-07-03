s = input()
v = 'aeiou'
d=[]
for i in v:
    if i not in s:
        d.append(i)
if len(d):
    print(*d,end=' ')
else:
    print("0")