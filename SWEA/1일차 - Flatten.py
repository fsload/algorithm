TC = 10
 
for t in range(TC):
    count = int(input())
    arr= list(map(int, input().split()))
 
    for i in range(count):
        maxIdx = arr.index(max(arr))
        arr[maxIdx] = max(arr) - 1
        minIdx = arr.index(min(arr))
        arr[minIdx] = min(arr) + 1
 
    print('#' + str(t+1), max(arr) - min(arr))
