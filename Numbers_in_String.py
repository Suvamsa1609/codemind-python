s=input()
sum=0
for i in s:
    if ord(i)>47 and ord(i)<58:
        sum+=int(i)
print(sum)