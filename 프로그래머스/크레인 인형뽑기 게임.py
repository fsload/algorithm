from collections import deque

def solution(board, moves):
    moves = deque(moves)
    board = list(map(list ,zip(*board)))
    stack = []
    answer = 0
    while moves:
        mv = moves.popleft()
        for i in range(len(board[mv-1])):
            if board[mv-1][i] != 0:
                stack.append(board[mv-1][i])
                board[mv-1][i] = 0
                break
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            answer = answer + 2
            stack.pop()
            stack.pop()

    return answer
