s=input()
ch=input()
c=0
for i in s:
    if ch==i:
        c+=1
if c==0:
    print("-1")
else:
    print(c)