def solution(n):
    answer = ''

    while n > 0:
        res, modul = divmod(n, 3)
        n = n // 3
        if modul == 0:
            modul = 4
            n = abs(n-1)
            print(n)
        answer = str(modul) + answer
    return answer
