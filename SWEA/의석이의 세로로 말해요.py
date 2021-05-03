TC = int(input())
 
for t in range(TC):
    arr = []
    MAX = -1
    for i in range(5):
        li = []
        li = list(input())
        if MAX < len(li):
            MAX = len(li)
        arr.append(li)
 
    print('#' + str(t+1), end= ' ')
    for j in range(MAX):
        for k in range(len(arr)):
            try:
                print(arr[k][j], end='')
            except IndexError:
                pass
    print(' ')
