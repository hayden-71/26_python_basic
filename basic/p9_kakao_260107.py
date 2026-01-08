# https://school.programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    stack = []

    for m in moves:
        for r in range(len(board)):
            if board[r][m - 1] != 0:  # 줄 타고 내려가면서 볼 애
                if stack and stack[-1] == board[r][m - 1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[r][m - 1])
                board[r][m - 1] = 0
                break
                # if len(stack) >= 2 and stack[-1] == stack[-2]:
                #     # del stack[-1]
                #     stack.pop()
                #     stack.pop()

    return answer


n = range(5, 31)
empty = 101

# 판 만들기

board = [empty for _ in range(len(n)) for _ in range(len(n))]
print(board)

# 그 안에 담긴 숫자 (0~100)
# 2개 이상이면 삭제

# https://school.programmers.co.kr/learn/courses/30/lessons/17679
EMPTY = "%"


def solution(m, n, board):
    answer = 0

    while True:
        mem = set()

        # 4개, 지울 애를 찾음
        for r in range(m - 1):
            for c in range(n - 1):
                if (
                    board[r][c]
                    == board[r][c + 1]
                    == board[r + 1][c]
                    == board[r + 1][c + 1]
                    and board[r][c] != EMPTY
                ):
                    mem |= set([(r, c), (r, c + 1), (r + 1, c), (r + 1, c + 1)])

        # 사라진 블록수 추가
        cnt = len(mem)
        if cnt == 0:
            break
        answer += cnt

        # 지우고 (r, c)
        for r, c in mem:
            board[r] = board[r][0:c] + EMPTY + board[r][c + 1 :]

        # 떨어트리고
        for r in range(m - 2, -1, -1):
            for c in range(n):
                if board[r][c] != EMPTY:
                    for r2 in range(m - 1, r, -1):
                        if board[r2][c] == EMPTY:
                            # SWAP
                            board[r2] = (
                                board[r2][0:c] + board[r][c] + board[r2][c + 1 :]
                            )
                            board[r] = board[r][0:c] + EMPTY + board[r][c + 1 :]

    return answer


board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
# CCBDE
# AAADE
# AAABF
# CCBBF
print(solution(4, 5, board))


# 다른 방식
# https://school.programmers.co.kr/learn/courses/30/lessons/17679


def pop_set(m, n, board):
    pop_set = set()
    for i in range(1, n):
        for j in range(1, m):
            if (
                board[i][j]
                == board[i - 1][j - 1]
                == board[i - 1][j]
                == board[i][j - 1]
                != "_"
            ):
                pop_set |= set([(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)])

    for i, j in pop_set:
        board[i][j] = 0
    for idx, row in enumerate(board):
        empty = ["_"] * row.count(0)
        board[idx] = empty + [block for block in row if block != 0]
    return len(pop_set)


def solution(m, n, board):
    # board = list(map(list, zip(*board)))
    my_board = []

    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(board[j][i])
        my_board.append(tmp)

    answer = 0
    while True:
        count = pop_set(m, n, my_board)
        if count == 0:
            return answer
        answer += count


if __name__ == "__main__":
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
