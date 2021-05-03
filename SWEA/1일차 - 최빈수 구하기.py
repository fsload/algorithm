TC = int(input())
 
for t in range(TC):
    num = int(input())
    arr = list(map(int, input().split()))
    count = [0]*101
    result = 0
    for item in arr:
        count[item] += 1
 
    maxCount = max(count)
 
    for i in range(len(count)):
        if count[i] == maxCount:
            result = i
 
    print('#' + str(t+1), result)
