dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
 
def dfs(nowY, nowX):
    global result
    if nowY == 13 and nowX == 13 and arr[nowY][nowX] == 3:
        result = 1
        return
    for i in range(4):
        X = nowX + dx[i]
        Y = nowY + dy[i]
        if arr[Y][X] == 0 and [Y, X] not in visited:
            visited.append([Y, X])
            dfs(Y, X)
            visited.pop()
        if arr[Y][X] == 3:
            result = 1
            return
 
for t in range(10):
    num = input()
    result = 0
    visited = []
    arr = []
    for i in range(16):
        li = list(map(int, input()))
        arr.append(li)
    visited.append([1, 1])
    dfs(1,1)
    print('#' + str(t + 1) ,result)
