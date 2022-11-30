s=input()
a=s.split()
min=999
for i in a:
    if len(i)<min:
        min=len(i)
print(min)