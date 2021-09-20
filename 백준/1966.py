import sys
from collections import deque

for i in range(int(sys.stdin.readline())):
    n, target = map(int, sys.stdin.readline().split())
    toPrint = deque(i for i in range(n))
    priority = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    while toPrint:
        if priority[0] == max(priority):
            toPop = toPrint.popleft()
            priority.popleft()
            cnt += 1
            if toPop == target:
                print(cnt)
        else:
            toPrint.append(toPrint.popleft())
            priority.append(priority.popleft())
