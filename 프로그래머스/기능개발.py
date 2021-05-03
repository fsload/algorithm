def solution(progresses, speeds):
    answer = []
    p = progresses
    s = speeds
    days = 0
    cnt = 0
    while p:
        if p[0] + s[0]*days >= 100:
            cnt += 1
            p.pop(0)
            s.pop(0)
        else:
            if cnt != 0:
                answer.append(cnt)
                cnt = 0
            days += 1
        if not p:
            answer.append(cnt)

    return answer
