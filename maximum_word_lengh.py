s=input()
a=s.split()
max=0
for i in a:
    if len(i)>max:
        max=len(i)
print(max)