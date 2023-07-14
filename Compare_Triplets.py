arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
alice = bob = 0
for i in range(len(arr1)):
    if arr1[i] > arr2[i]:
        alice+=1
    elif arr1[i] < arr2[i]:
        bob+=1
print(alice,bob)