from collections import deque
 
TC = 10
dx = [1,-1,0,0]
dy = [0,0,1,-1]
 
 
def bfs(maze):
    visited = []
    queue = deque()
 
    queue.append([1, 1])
 
    while queue:
        x, y = queue.popleft()
        if maze[x][y] == '3':
            return 1
        visited.append([x, y])
 
        for i in range(4):
            nX = x + dx[i]
            nY = y + dy[i]
 
            if 0 <= nX < 16 and 0 <= nY < 16:
                if maze[nX][nY] != '1' and [nX,nY] not in visited:
                    queue.append([nX, nY])
 
    return 0
 
for T in range(TC):
    num = input()
    maze = []
    for _ in range(16):
        li = input()
        li = list(li)
        maze.append(li)
 
    print('#'+str(num), bfs(maze))
