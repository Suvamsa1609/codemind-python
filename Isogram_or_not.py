s = input()
flag = 1
for i in s:
    if s.count(i) != 1:
        flag = 0
        break
if flag == 1:
    print(True)
else:
    print(False)