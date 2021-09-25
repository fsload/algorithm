num = int(input())

cnt = 0
for n in range(num+1):
    if n>=125 and n%125 == 0:
        cnt += 3
    elif n>=25 and n%25 == 0:
        cnt += 2
    elif n>=5 and n%5 == 0:
        cnt += 1
print(cnt)
