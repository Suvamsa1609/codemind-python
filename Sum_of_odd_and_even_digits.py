n=int(input())
d=list(map(int,input().split()))
o_sum=e_sum=0
for i in range(n):
    if i%2:
        o_sum=o_sum+d[i]
    else:
        e_sum=e_sum+d[i]
if o_sum-e_sum:
    print("NO")
else:
    print("YES")