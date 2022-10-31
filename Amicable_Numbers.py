def factors(num):
    s=0
    for i in range(1,num):
        if num%i==0:
            s=s+i
    return s
n=int(input())
m=int(input())
if factors(n)==m and factors(m)==n:
    print("Amicable")
else:
    print("Not Amicable")
