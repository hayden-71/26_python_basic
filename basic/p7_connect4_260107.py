# 세로, 가로 칸 보드 만들기
# 하나의 ㅇ에 경우의 수는 3가지
# 누구의 턴인지
# 4목이 되면 끝나기
# 혹은 게임판이 다 차면 끝

RED = 100
BLACK = 101
EMPTY = 102

DRAW = 103
NOTYET = 104

WIDTH = 7
HEIGHT = 6

board = [[EMPTY] * WIDTH for _ in range(HEIGHT)]
turn = RED


def print_board(board):
    # for i in range(HEIGHT):
    #     for j in range(WIDTH)
    print("1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣")
    for r in board:  # 몇번째 줄
        for c in r:  # 몇번째 칸
            if c == EMPTY:
                print("⚪", end="")
            elif c == RED:
                print("🟠", end="")
            else:
                print("⚫", end="")
        print("")


# board: 판떼기
# col: 1~7, 몇 번째 줄에 놓을건지
# turn: 현재 돌을 놓은 사람
# return: True 돌을 성공적으로 놓음 / False 해당 줄이 꽉차서 놓지 못함
def drop(board, col, turn):
    col = int(col)  # 숫자라고 명명하기
    for i in range(HEIGHT - 1, -1, -1):
        if board[i][col - 1] == EMPTY:
            board[i][col - 1] = turn
            return True
    return False


# return
# RED, BLACK, DRAW, NOTYET
def check_end(board):
    # 가로 체크
    for i in range(HEIGHT):
        for j in range(WIDTH - 4 + 1):
            if (
                board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3]
                and board[i][j] != EMPTY
            ):
                return board[i][j]

    # 세로 체크
    for i in range(HEIGHT - 4 + 1):
        for j in range(WIDTH):
            if (
                board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j]
                and board[i][j] != EMPTY
            ):
                return board[i][j]

    # 대각 \ 체크
    for i in range(HEIGHT - 4 + 1):
        for j in range(WIDTH - 4 + 1):
            if (
                board[i][j]
                == board[i + 1][j + 1]
                == board[i + 2][j + 2]
                == board[i + 3][j + 3]
                and board[i][j] != EMPTY
            ):
                return board[i][j]

    # 대각 / 체크
    for i in range(HEIGHT - 4 + 1):
        for j in range(4 - 1, WIDTH):
            if (
                board[i][j]
                == board[i + 1][j - 1]
                == board[i + 2][j - 2]
                == board[i + 3][j - 3]
                and board[i][j] != EMPTY
            ):
                return board[i][j]

    # 꽉 참 체크
    for r in board:
        if r.count(EMPTY) != 0:
            return NOTYET  # 각 줄을 보고 0이 아닌게 있으면 아직 하는 중
    # if board[0].count(EMPTY) != 0: return NOTYET
    return DRAW


while True:
    print_board(board)
    user = input(f"{"RED" if turn == RED else "BLACK"} input:")
    if drop(board, user, turn):
        turn = RED if turn == BLACK else BLACK
        result = check_end(board)
        if result != NOTYET:
            print_board(board)
            if result == DRAW:
                print("비겼습니다")
            else:
                print(f"{"RED" if result == RED else "BLACK"} 승리!")
            break
