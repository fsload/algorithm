def solution(priorities, location):
    p = priorities
    nowpoint = p.index(max(p))

    cnt = 0
    stack = []
    while True:
        if nowpoint == location and p[nowpoint] == max(p):
            cnt += 1
            break
        if p[nowpoint] == max(p):
            p[nowpoint] = 0
            cnt += 1
        elif nowpoint == len(p) - 1:
            nowpoint = 0
        else:
            nowpoint += 1

    answer = cnt
    return answer
