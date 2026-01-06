# 5x5 미로 (0:길, 1:벽, 2:도착점)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 2],
]

# 플레이어 시작 위치 (0행 0열)
y, x = 0, 0

while True:
    # 1. 미로 출력하기 (현재 상태 보여주기)
    print("\n" * 10)  # 화면 깨끗하게 밀기(편법)
    print("=== 미로 탈출 게임 ===")

    for i in range(len(maze)):  # 세로줄(행) 반복
        for j in range(len(maze[i])):  # 가로줄(열) 반복
            if i == y and j == x:
                print("🐹", end=" ")  # 플레이어
            elif maze[i][j] == 1:
                print("⬛", end=" ")  # 벽
            elif maze[i][j] == 2:
                print("🚩", end=" ")  # 도착점
            else:
                print("⬜", end=" ")  # 길
        print()  # 줄바꿈

    # 2. 도착 확인
    if maze[y][x] == 2:
        print("🎉 탈출 성공! 고생하셨습니다! 🎉")
        break

    # 3. 이동 입력 받기
    move = input("이동(w:위, s:아래, a:왼쪽, d:오른쪽) > ")

    # 4. 이동 로직 (다음 위치 미리 계산)
    next_y, next_x = y, x

    if move == "w":
        next_y -= 1
    elif move == "s":
        next_y += 1
    elif move == "a":
        next_x -= 1
    elif move == "d":
        next_x += 1

    # 5. 유효성 검사 (맵 밖으로 나가는지? 벽인지?)
    # 인덱스 범위 체크 (이게 제일 중요합니다!)
    if 0 <= next_y < len(maze) and 0 <= next_x < len(maze[0]):
        # 벽이 아니면 이동 승인
        if maze[next_y][next_x] != 1:
            y, x = next_y, next_x
        else:
            print("🛑 쿵! 벽입니다.")
    else:
        print("🚫 맵 밖으로 나갈 수 없습니다.")
