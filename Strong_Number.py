import math
n = input()
sum = 0
for i in n:
    d = math.factorial(int(i))
    sum+=d
if int(n) == sum:
    print("The number {} is a strong number".format(n))
else:
    print("The number {} is not a strong number".format(n))