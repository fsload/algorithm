TC = int(input())
 
for t in range(TC):
    sdoku = []
    for i in range(9):
        li = []
        li = list(map(int, input().split()))
        sdoku.append(li)
 
    #check row
    result = 1
    for i in range(9):
        if sum(sdoku[i]) != 45:
            result = 0
 
    #check col
    sawpArr = list(map(list, zip(*sdoku)))
 
    if result != 0:
        for i in range(9):
            if sum(sawpArr[i]) != 45:
                result = 0
 
 
    if result != 0:
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                chk = 0
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        chk += sdoku[x][y]
                if chk != 45:
                    result = 0
 
 
    print('#'+ str(t+1), result)
