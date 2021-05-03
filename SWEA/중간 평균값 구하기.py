TC = int(input())
for t in range(TC):
    arr = list(map(int, input().split()))
    arr.remove(max(arr))
    arr.remove(min(arr))
 
    print('#'+ str(t+1), int(((sum(arr)) + 4) / 8))
