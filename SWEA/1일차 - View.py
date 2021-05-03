for t in range(10):
    length = int(input())
    arr = list(map(int, input().split()))
    sum = 0
    for i in range(2, len(arr) -2):
        view = arr[i] - max(arr[i-1], arr[i-2], arr[i+1], arr[i+2])
        if view >= 1:
            sum += view
             
    print('#' + str(t+1), sum)
