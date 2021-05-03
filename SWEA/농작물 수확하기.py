TC = int(input())
 
for t in range(TC):
    size = int(input())
    arr = []
    for i in range(size):
        li = []
        li = list(map(int, input()))
        arr.append(li)
 
    sum1 = 0
    cnt = 0
    for i in range(size):
        if i < int(size/2):
            for j in range(int(size/2)-i, int(size/2)+i+1):
                # print(i, j, arr[i][j])
                sum1 += arr[i][j]
 
        elif i > int(size/2):
            cnt += 1
            for k in range(cnt, size - cnt):
                # print(i, k, arr[i][k])
                sum1 += arr[i][k]
        else:
            # print(i)
            sum1 += sum(arr[i])
    print('#' + str(t+1), sum1)
