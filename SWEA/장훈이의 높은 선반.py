def dfs(index, nowTall):
    global result
 
    if index == number:
        if tall <= nowTall < result:
            result = nowTall
        return
 
    else:
        visited[index] = 1
        dfs(index+1, nowTall + arr[index] * visited[index])
        visited[index] = 0
        dfs(index+1, nowTall + arr[index] * visited[index])
TC = int(input())
 
for t in range(TC):
    number, tall = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * number
 
    result = 100000
    dfs(0, 0)
    print(f'#{t+1} {result - tall}')
