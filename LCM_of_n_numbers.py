def lcm_2(a,b):
    i = 1
    while 1:
        m = b*i
        if m%a == 0:
            return m
        i+=1

def lcm_n(lst):
    l = 1
    for i in lst:
        l = lcm_2(l,i)
    return l
    
n = int(input())
lst = list(map(int,input().split()))
print(lcm_n(lst))