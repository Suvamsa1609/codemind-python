s=input()
vc=cc=dc=sc=0
v='aeiou'
for i in s:
    if i==" ":
        sc+=1
    elif i in v:
        vc+=1
    elif i.isdigit():
        dc+=1
    else:
        cc+=1
print("Vowels:",vc)
print("Consonants:",cc)
print("Digits:",dc)
print("White spaces:",sc)