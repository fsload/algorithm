N = int(input())
li = []
for i in range(N):
    li.append(i+1)
print(li)

ans = []
index = 0
while li:
    num = int(input())
    if num not in li:
        print('NO')
        break
    while True:

        print(li, index)
        print(ans)
        if num > li[index]:
            index += 1
            ans.append('+')

        elif num < li[index]:
            index -= 1
            li.pop(index)
            ans.append('-')
    print(li.pop(index))
