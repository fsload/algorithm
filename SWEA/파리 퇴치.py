TC = int(input())
for t in range(TC):
    arrSize, killSize = input().split()
 
    arrSize = int(arrSize)
    killSize = int(killSize)
    arr = []
    kill = -1
    for size in range(arrSize):
        li = list(map(int, input().split()))
        arr.append(li)
 
    for i in range(arrSize - killSize + 1):
        for j in range(arrSize - killSize + 1):
            totKill = 0
            for x in range(i, i+killSize):
                for y in range(j, j+killSize):
                    totKill += arr[x][y]
            if totKill >= kill:
                kill = totKill
 
    print('#' + str(t + 1), kill)
