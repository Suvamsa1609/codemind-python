import math
def triangle(a,b,c):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area
a,b,c=map(int,input().split())
print("%.2f"%triangle(a,b,c))