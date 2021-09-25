N = int(input())
li = []
for i in range(N):
    li.append(i+1)

ans = ['+']
index = 0
nums = []
for i in range(N):
    nums.append(int(input()))

for num in nums:
    if num not in li:
        print('NO')
        ans = []
        break
    while True:
        if num > li[index]:
            index += 1
            ans.append('+')

        elif num < li[index]:
            li.pop(index)
            index -= 1
            ans.append('-')
        else:
            li.pop(index)
            ans.append('-')
            if index > 0:
                index -= 1
            break
if ans != []:
    for item in ans:
        print(item)
