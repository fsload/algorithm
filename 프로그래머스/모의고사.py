def solution(answers):
    answer = []
    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans1 = 0
    ans2 = 0
    ans3 = 0
    if len(answers) <= 10:
        answers.append(0)
        answers.append(0)
        answers.append(0)
        answers.append(0)
        answers.append(0)
        answers.append(0)
        answers.append(0)
        answers.append(0)
        answers.append(0)
        answers.append(0)
    for i in range(len(answers)):
        if answers[i] == std1[i % 5]:
            ans1 += 1
        if answers[i] == std2[i % 8]:
            ans2 += 1
        if answers[i] == std3[i % 10]:
            ans3 += 1
    m = max(ans1, ans2, ans3)

    if ans1 == m:
        answer.append(1)
    if ans2 == m:
        answer.append(2)
    if ans3 == m:
        answer.append(3)

    return answer
