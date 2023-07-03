s = input()
v_lower = 'aeiou'
v_upper = 'AEIOU'
a = ''
b = ''
for i in v_lower:
    if i in s:
        a+=i
for i in v_upper:
    if i in s:
        b+=i
if a == v_lower or b == v_upper:
    print(True)
else:
    print(False)