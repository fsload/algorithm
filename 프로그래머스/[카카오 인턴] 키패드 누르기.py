arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]

def getDis(handPos, toClick):
    if toClick == 2:
        clickPos = [0, 1]
    elif toClick == 5:
        clickPos = [1, 1]
    elif toClick == 8:
        clickPos = [2, 1]
    elif toClick == 0:
        clickPos = [3, 1]

    dis = abs(handPos[0] - clickPos[0]) + abs(handPos[1] - clickPos[1])

    return dis


def solution(numbers, hand):

    leftPos = [3, 0]
    rightPos = [3, 2]

    answer = ''
    for num in numbers:
        if num == 1 or num == 2 or num == 3:
            Ypos = 0
            Xpos = arr[0].index(num)
            if num == 1:
                leftPos = [Ypos, Xpos]
                answer += 'L'

            elif num == 2:
                if getDis(leftPos, 2) > getDis(rightPos, 2):
                    rightPos = [Ypos, Xpos]
                    answer += 'R'
                elif getDis(leftPos, 2) < getDis(rightPos, 2):
                    leftPos = [Ypos, Xpos]
                    answer += 'L'

                elif getDis(leftPos, 2) == getDis(rightPos, 2):
                    if hand == "right":
                        rightPos = [Ypos, Xpos]
                        answer += 'R'

                    else:
                        leftPos = [Ypos, Xpos]
                        answer += 'L'

            else:
                rightPos = [Ypos, Xpos]
                answer += 'R'

        elif num == 4 or num == 5 or num == 6:
            Ypos = 1
            Xpos = arr[1].index(num)
            if num == 4:
                leftPos = [Ypos, Xpos]
                answer += 'L'

            elif num == 5:
                if getDis(leftPos, 5) > getDis(rightPos, 5):
                    rightPos = [Ypos, Xpos]
                    answer += 'R'

                elif getDis(leftPos, 5) < getDis(rightPos, 5):
                    leftPos = [Ypos, Xpos]
                    answer += 'L'

                elif getDis(leftPos, 5) == getDis(leftPos, 5):
                    if hand == "right":
                        rightPos = [Ypos, Xpos]
                        answer += 'R'

                    else:
                        leftPos = [Ypos, Xpos]
                        answer += 'L'

            else:
                rightPos = [Ypos, Xpos]
                answer += 'R'

        elif num == 7 or num == 8 or num == 9:
            Ypos = 2
            Xpos = arr[2].index(num)
            if num == 7:
                leftPos = [Ypos, Xpos]
                answer += 'L'

            elif num == 8:
                if getDis(leftPos, 8) > getDis(rightPos, 8):
                    rightPos = [Ypos, Xpos]
                    answer += 'R'

                elif getDis(leftPos, 8) < getDis(rightPos, 8):
                    leftPos = [Ypos, Xpos]
                    answer += 'L'

                elif getDis(leftPos, 8) == getDis(rightPos, 8):
                    if hand == "right":
                        rightPos = [Ypos, Xpos]
                        answer += 'R'

                    else:
                        leftPos = [Ypos, Xpos]
                        answer += 'L'

            else:
                rightPos = [Ypos, Xpos]
                answer += 'R'

        elif num == 0:
            if getDis(leftPos, 0) > getDis(rightPos, 0):
                rightPos = [3, 1]
                answer += 'R'

            elif getDis(leftPos, 0) < getDis(rightPos, 0):
                leftPos = [3, 1]
                answer += 'L'

            elif getDis(leftPos, 0) == getDis(rightPos, 0):
                if hand == "right":
                    rightPos = [3, 1]
                    answer += 'R'

                else:
                    leftPos = [3, 1]
                    answer += 'L'

    return answer
