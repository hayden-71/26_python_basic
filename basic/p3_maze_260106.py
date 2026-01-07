# 1 : 벽
# 0 : 길
# 3 : 골
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
]

# 쥐에게 'x, y, 방향' 3가지가 있어야 됨
# 북동남서
N, E, S, W = 100, 101, 102, 103

mouse = {"x": 1, "y": 1, "direction": S}

import os
import time


def print_maze():
    global maze
    global mouse
    os.system("cls" if os.name == "nt" else "clear")
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if i == mouse["y"] and j == mouse["x"]:
                print("🐹", end="")
            elif maze[i][j] == 1:
                print("🧱", end="")
            elif maze[i][j] == 2:
                print("🚩", end="")
            elif maze[i][j] == 3:
                print("🏁", end="")
            else:
                print("  ", end="")
        print("")


def move_mouse():
    global mouse  # 글로벌로 쓸거야! 선언
    global maze

    # 남쪽 볼 때
    if mouse["direction"] == S:
        # 동
        if maze[mouse["y"]][mouse["x"] + 1] in [0, 3]:
            mouse["x"] = mouse["x"] + 1
            mouse["direction"] = E
        # 남
        elif maze[mouse["y"] + 1][mouse["x"]] in [0, 3]:
            mouse["y"] = mouse["y"] + 1
            mouse["direction"] = S
        # 서
        elif maze[mouse["y"]][mouse["x"] - 1] in [0, 3]:
            mouse["x"] = mouse["x"] - 1
            mouse["direction"] = W
        # 북
        else:
            mouse["y"] = mouse["y"] - 1
            mouse["direction"] = N

    elif mouse["direction"] == E:
        # 동쪽 볼 때 (북>동>남>서)
        # 북
        if maze[mouse["y"] - 1][mouse["x"]] in [0, 3]:
            mouse["y"] -= 1
            mouse["direction"] = N
        # 동
        elif maze[mouse["y"]][mouse["x"] + 1] in [0, 3]:
            mouse["x"] = mouse["x"] + 1
            mouse["direction"] = E
        # 남
        elif maze[mouse["y"] + 1][mouse["x"]] in [0, 3]:
            mouse["y"] = mouse["y"] + 1
            mouse["direction"] = S
        # 서
        else:
            mouse["x"] = mouse["x"] - 1
            mouse["direction"] = W

    elif mouse["direction"] == W:
        # 서쪽 볼 때 (남>서>북>동)
        # 남
        if maze[mouse["y"] + 1][mouse["x"]] in [0, 3]:
            mouse["y"] = mouse["y"] + 1
            mouse["direction"] = S
        # 서
        elif maze[mouse["y"]][mouse["x"] - 1] in [0, 3]:
            mouse["x"] = mouse["x"] - 1
            mouse["direction"] = W
        # 동
        elif maze[mouse["y"]][mouse["x"] - 1] in [0, 3]:
            mouse["x"] = mouse["x"] - 1
            mouse["direction"] = N
        # 북
        else:
            mouse["x"] = mouse["x"] + 1
            mouse["direction"] = E
    else:
        # 북쪽 볼 때 (서>북>동>남)
        # 서
        if maze[mouse["y"]][mouse["x"] - 1] in [0, 3]:
            mouse["x"] = mouse["x"] - 1
            mouse["direction"] = W
        # 북
        elif maze[mouse["y"] - 1][mouse["x"]] in [0, 3]:
            mouse["y"] -= 1
            mouse["direction"] = N
        # 동
        elif maze[mouse["y"]][mouse["x"] + 1] in [0, 3]:
            mouse["x"] = mouse["x"] + 1
            mouse["direction"] = E
        # 남
        else:
            mouse["y"] = mouse["y"] + 1
            mouse["direction"] = S


while maze[mouse["y"]][mouse["x"]] != 3:
    print_maze()
    move_mouse()

    time.sleep(0.2)
# 특정 작업을 일정 시간동안 지연시키고자 할 때
# 코드 실행 간격을 조절하고자 할 때
# 반복문에서 일정한 간격으로 작업을 수행하고자 할 때
