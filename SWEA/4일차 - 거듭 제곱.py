def pow(num, nowCnt, res):
    global result
    if nowCnt == count:
        result = res
        return
    pow(num, nowCnt+1, res * num)
 
for t in range(10):
    result = 0
    tc = input()
    toPow, count = input().split()
    toPow = int(toPow)
    count = int(count)
 
    pow(toPow, 0, 1)
 
    print('#' + tc, result)
