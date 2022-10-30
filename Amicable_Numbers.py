def factors(num):
    s=0
    for i in range(1,num):
        if num%i==0:
            s=s+i
    return s
n=int(input())
m=int(input())
if n==factors(m) and m==factors(n):
    print("Amicable")
else:
    print("Not Amicable")