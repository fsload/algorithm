TC = 10
 
for t in range(TC):
    num = input()
    li = list(map(int, (input().split())))
    tmp = 0
    while li[7] > 0:
        for i in range(1, 6):
            li.append(0)
            li[0] = li[0]-i
            if li[0] <= 0:
                li[8] = li[0]
                li = li[1:]
                break
            else:
                li[8] = li[0]
                li = li[1:]
    li = map(str, li[:7])
    print('#'+num ,' '.join(li)+' 0')
