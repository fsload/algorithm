def isPalin(arr):
    for i in range(int(len(arr)/2)):
        if arr[i] != arr[-1-i]:
            return False
 
    return True
 
for t in range(10):
    size = int(input())
    arr = []
    for i in range(8):
        li = list(input())
        arr.append(li)
 
    count = 0
 
    for i in range(8):
        for j in range(8 - size + 1):
            if isPalin(arr[i][j:j + size]):
                count += 1
 
    arr = list(map(list, zip(*arr)))
 
    for i in range(8):
        for j in range(8 - size + 1):
            if isPalin(arr[i][j: j + size]):
                count += 1
    print('#' + str(t+1), count)
