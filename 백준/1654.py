K, N = map(int, input().split())

line = []

for i in range(K):
    line.append(int(input()))
start, end = 1, max(line)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for li in line:
        cnt += li // mid

    if cnt < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)
