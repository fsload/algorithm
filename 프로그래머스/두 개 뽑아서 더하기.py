from itertools import combinations as cb
def solution(numbers):
    arr = list(cb(numbers, 2))
    answer = []

    for a, b in arr:
        if a + b not in answer:
            answer.append(a+b)
    answer.sort()
    return answer
