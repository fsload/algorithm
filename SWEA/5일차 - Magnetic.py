for t in range(10):
    size = int(input())
    arr = []
    for i in range(size):
        li = list(map(int, input().split()))
        arr.append(li)
 
    arr = list(map(list, zip(*arr)))
    count = 0
 
    for i in range(len(arr)):
        stack = []
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                stack.append(1)
            if arr[i][j] == 2 and stack:
                stack.clear()
                count += 1
 
    print('#' + str(t+1), count)
