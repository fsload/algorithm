from collections import deque
 
def findNext(map, node, dis):
    dis += 1
    nextNode = []
    for x, y in map:
        if x == node:
            nextNode.append(y)
    return nextNode, dis
def bfs(map, st):
    next_ = []
    queue = deque()
    queue.append([st,0])
    visited = []
    maxi = -1
    dist = 0
    dis = 0
    while queue:
        node, dis = queue.popleft()
        if node not in visited:
            if dis > dist:
                dist = dis
                maxi = int(node)
            if dis == dist and maxi < int(node):
                maxi = int(node)
            visited.append(node)
            next_, dis = findNext(map, node, dis)
            for nod in next_:
                queue.append([nod,dis])
 
    return maxi
for t in range(10):
    long, start = input().split()
    arr = list(input().split(' '))
    map = []
    for i in range(int(len(arr)/2)):
        li = []
        li.append(arr[i*2])
        li.append(arr[i*2+1])
        if li not in map:
            map.append(li)
 
    maxNode = bfs(map,start)
 
    print('#' + str(t+1), maxNode)
