n = int(input())
lst = list(map(int,input().split()))
d = lst[::]
lst.sort()
lst.reverse()
if d == lst:
    print('yes')
else:
    print('no')