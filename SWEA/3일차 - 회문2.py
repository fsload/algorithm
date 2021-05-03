def isPalin(arr):
    for i in range(int(len(arr)/2)):
        if arr[i] != arr[-1-i]:
            return False
    return True
for t in range(10):
    num = input()
    arr = []
    for i in range(100):
        li = list(input())
        arr.append(li)
 
    result = -1
 
    for i in range(100):
        for j in range(100):
            for k in range(100-j + 1):
                if isPalin(arr[i][j:j+k]):
                    if k > result:
                        result = k
 
    arr = list(map(list, zip(*arr)))
 
 
    for i in range(100):
        for j in range(100):
            for k in range(100-j + 1):
                if isPalin(arr[i][j:j+k]):
                    if k > result:
                        result = k
 
    print('#' + num, result)
