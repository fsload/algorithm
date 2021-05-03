def solution(array, commands):
    answer = []
    for cmd in commands:
        sparr = array[cmd[0]-1: cmd[1]]
        sparr = sorted(sparr)
        answer.append(sparr[cmd[2] - 1])
    return answer
