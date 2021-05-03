from collections import deque
TC = int(input())
 
prizeAfterCount = []
visited = []
 
def dfs(nowCount):
    nowCount = int(nowCount)
 
 
    while prizeAfterCount:
        nowPrize, nowCount = prizeAfterCount.popleft()
        nowCount = int(nowCount)
        nowCount -= 1
        if int(nowCount) == -1:
            li = []
            li.append(nowPrize)
            for x, y in prizeAfterCount:
                if y == 0:
                    li.append(x)
            break
        else :
            for i in range(len(nowPrize)):
                for j in range(i + 1, len(nowPrize)):
                    toSwap = nowPrize
                    toSwap = list(toSwap)
                    toSwap[i] , toSwap[j] = toSwap[j], toSwap[i]
                    toSwap = ''.join(toSwap)
                    if toSwap not in prizeAfterCount and toSwap != None and [toSwap, nowCount] not in prizeAfterCount:
                        prizeAfterCount.append([toSwap, nowCount])
    print('#' + str(t+1), max(li))
 
 
 
for t in range(TC):
    nowPrize, count = input().split()
    nowCount = count
    prizeAfterCount = deque()
    prizeAfterCount.append([nowPrize, nowCount])
    result = dfs(nowCount)
    prizeAfterCount = []
