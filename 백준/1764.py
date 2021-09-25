import sys
N, M = list(map(int, sys.stdin.readline().split()))
setA = set()
setB = set()
for _ in range(N):
    setA.add(sys.stdin.readline().strip())

for _ in range(M):
    setB.add(sys.stdin.readline().strip())

newSet = setA & setB

li = sorted(newSet)
print(len(li))
for item in li:
    print(item)
