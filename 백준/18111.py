import sys
N, M, B = map(int, sys.stdin.readline().split())
li = []
for i in range(N):
    lis = list(map(int, sys.stdin.readline().split()))
    li.append(lis)
ans = 10000000000000000000
for i in range(257):
    cntOver = 0
    cntUnder = 0
    for y in range(N):
        for x in range(M):
            if li[y][x] < i:
                cntUnder += i-li[y][x]
            elif li[y][x] > i:
                cntOver += li[y][x]-i
    cntBlock = B + cntOver - cntUnder
    if cntBlock < 0:
        continue
    nowTime = 2*cntOver + cntUnder
    if nowTime <= ans:
        ans = nowTime
        height = i
print(ans, height)
