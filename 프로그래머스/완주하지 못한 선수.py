def solution(p, c):
    dicP = dict()
    dicC = dict()
    for per in p:
        if per in dicP:
            dicP[per] += 1
        else:
            dicP.update({f'{per}': 1})

    for per in c:
        if per in dicC:
            dicC[per] += 1
        else:
            dicC.update({f'{per}': 1})
    for key,val in dicC.items():
        if key in dicP:
            dicP[key] -= val
    for key, val in dicP.items():
        if val == 1:
            return key
