TC = int(input())
for t in range(TC):
    day = int(input())
    arr = list(map(int, input().split()))
     
    MAX = arr[-1]
    cnt = 0
    for i in range(day - 1, -1, -1):
        if MAX > arr[i]:
            cnt += MAX - arr[i]
        else:
            MAX = arr[i]
 
    print('#'+ str(t+1), cnt)
