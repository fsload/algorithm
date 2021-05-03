TC = int(input())
 
for t in range(TC):
    a, b = input().split()
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
 
    if len(arr1) < len(arr2):
        smallArr = arr1
        bigArr = arr2
    else:
        smallArr = arr2
        bigArr = arr1
    maxPro = -10000
    for i in range(len(bigArr)-len(smallArr) + 1):
        product = 0
        for j in range(len(smallArr)):
            product += smallArr[j] * bigArr[i+j]
        if product > maxPro:
            maxPro = product
 
    print('#'+ str(t+1), maxPro)
