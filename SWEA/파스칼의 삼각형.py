TC = int(input())
 
for t in range(TC):
    n = int(input())
    arr = []
    for i in range(n):
        if i == 0:
            arr.append([1])
        else:
            li = []
            for j in range(i+1):
                if j == 0 or j == i:
                    li.append(1)
                else:
                    li.append(arr[i - 1][j - 1] + arr[i - 1][j])
            arr.append(li)
 
    print('#'+ str(t+1))
    for item in arr:
        item = ''.join(str(item))
        item = item.replace('[', '')
        item = item.replace(']', '')
        item = item.replace(',', '')
 
        print(item)
