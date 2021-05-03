def solution(n, lost, reserve):
    toDel = set(reserve) & set(lost)
    reserve = list(set(reserve) - toDel)
    lost = list(set(lost) - toDel)
    cnt = n - len(lost) - len(reserve)
    print(cnt, lost, reserve)
    for item in sorted(reserve, reverse=True):
        if item + 1 in lost:
            cnt += 1
            lost.remove(item+1)
        elif item - 1 in lost:
            cnt += 1
            lost.remove(item-1)
    
    cnt += len(reserve)
    return cnt
