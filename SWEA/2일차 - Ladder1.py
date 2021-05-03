dx = [-1, 1, 0]
dy = [0, 0, 1]
 
 
def dfs(nowY, nowX):
    global result
    visited.append([nowX, nowY])
 
    if nowY == 99:
        result = nowX
        return
 
    for i in range(3):
        X = nowX + dx[i]
        Y = nowY + dy[i]
        if 0 <= X < 100 and 0 <= Y < 100 and arr[Y][X] == 1:
            if [X, Y] not in visited:
                return dfs(Y, X)
 
 
 
for t in range(10):
    result = 0
    num = input()
    arr = []
 
    for i in range(100):
        li = list(map(int, input().split()))
        arr.append(li)
    arr.reverse()
    visited = []
    stack = []
    start = arr[0].index(2)
    dfs(0, start)
    print('#' + num, result)
