for t in range(10):
    num = int(input())
    arr = []
    for i in range(100):
        li = []
        li = list(map(int, input().split()))
        arr.append(li)
    result = 0
 
    #get row sum
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr[i])):
            sum += arr[i][j]
        if result < sum:
            result = sum
 
    #get diagonal sum
    sum = 0
    for i in range(len(arr)):
        sum += arr[i][i]
    if result < sum:
        result = sum
    sum = 0
    for i in range(99, -1, -1):
        sum += arr[i][i]
    if result < sum:
        result = sum
 
    #get col sum
 
    arr = list(map(list, zip(*arr)))
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr[i])):
            sum += arr[i][j]
        if result < sum:
            result = sum
             
    print('#' + str(num), result)
