TC = int(input())
 
for t in range(TC):
    line, size = input().split()
    line = int(line)
    size = int(size)
    arr = []
    for i in range(line):
        li = []
        li = list(map(int, input().split()))
        arr.append(li)
    result = 0
    for i in range(line):
        count = 0
        for j in range(line):
            if arr[i][j] == 1:
                count += 1
            else:
                count = 0
            try:
                if count == size and arr[i][j+1] == 0:
                    result += 1
            except IndexError:
                result += 1
            # if count == size:
            #     result += 1
 
    arr = list(map(list, zip(*arr)))
 
 
 
    for i in range(line):
        count = 0
        for j in range(line):
            if arr[i][j] == 1:
                count += 1
            else:
                count = 0
            try:
                if count == size and arr[i][j+1] == 0:
                    result += 1
            except IndexError:
                if count == size:
                    result += 1
            # if count == size:
            #     result += 1
    print('#'+ str(t+1), result)
