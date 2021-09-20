import sys

N, target = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(trees)

while start <= end:
    mid = (start+end) // 2
    sum = 0
    for tree in trees:
        if tree > mid:
            sum += tree - mid

    if sum >= target:
        start = mid + 1
    else:
        end = mid - 1
print(end)
