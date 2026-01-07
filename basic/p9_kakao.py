# https://school.programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    stack = []

    for m in moves:
        for r in range(len(board)):
            if board[r][m - 1] != 0: # 줄 타고 내려가면서 볼 애
                if stack and stack[-1] == board[r][m-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[r][m-1])
                board[r][m-1] = 0
                break
                # if len(stack) >= 2 and stack[-1] == stack[-2]:
                #     # del stack[-1]
                #     stack.pop()
                #     stack.pop()
    
    return answer


# n = range(5, 31)
# empty = 101

# # 판 만들기

# board = [empty for _ in range(len(n)) for _ in range(len(n))]
# print(board)

# # 그 안에 담긴 숫자 (0~100)
# # 2개 이상이면 삭제

# https://school.programmers.co.kr/learn/courses/30/lessons/17679
EMPTY = %

def solution(m, n, board):
    answer = 0
    mem = set()
    # 4개 지울 애를 찾음
    for i in range(m - 1):
        for j in range(n -1):
            if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] \
                and board[i][j] != EMPTY:
            mem.union(set[(r, c), (r, c + 1), (r + 1, c), (r + 1, c + 1)])
    # 지우고
    # 사라진 블럭 수 추가
    answer = len(mem)
    # 떨어트리고
    
    return answer