TC = int(input())
for i in range(TC):
    arr = input()
    cnt = 1
    li = ""
    flag = False
 
    while 1:
        li = arr[:cnt]
        if cnt == 10:
            break
        for j in range(cnt, len(arr), cnt):
            if li != arr[j:j + cnt]:
                break
            else:
                flag = True
                break
 
        if flag:
            break
 
        cnt += 1
 
    print("#" + str(i+1), len(li)
