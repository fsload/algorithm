def dfs(now, next):
    visited.append([now, next])
    stack.append([now, next])
    global result
    if next == 99:
        result = 1
        return
    if stack:
        stack.pop()
        for item in arr:
            if item[0] == next and [item[0], item[1]] not in visited:
                dfs(item[0], item[1])
    return
 
 
for t in range(10):
    visited = []
    stack = []
    result = 0
    a, b = input().split()
    arr = []
    li = list(map(int, input().split()))
 
    for i in range(0, len(li), 2):
        lis = [li[i], li[i+1]]
        arr.append(lis)
    dfs(arr[0][0], arr[0][1])
    print('#' + str(t+1), result)
