def solution(a, b):
    date = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = {1 : 31, 2 : 29, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 :31}
    tot = 0
    for key, val in month.items():
        if key < a:
            tot += val
    tot += b
    idx = tot % 7
    answer = date[idx]
    return answer
