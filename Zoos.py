s=input()
x=y=0
for i in s:
    if i=='z':
        x+=1
    else:
        y+=1
if 2*x==y:
    print("Yes")
else:
    print("No")