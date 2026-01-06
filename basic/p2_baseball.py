import random


def generate_number():
    digits = random.sample(range(0, 10), 3)
    return "".join(map(str, digits))


def check_input(answer, input):
    result = {"strike": 0, "ball": 0}

    for i in range(3):
        if input[i] == answer[i]:
            result["strike"] += 1
        elif input[i] in answer:
            result["ball"] += 1

    return result


def play_game():
    print("=== 숫자 야구 게임 ===")
    answer = generate_number()
    count = 0

    while True:
        user_input = input("숫자 3자리를 입력하세요: ")

        # 입력 검증
        if (
            not user_input.isdigit()
            or len(user_input) != 3
            or len(set(user_input)) != 3
        ):
            print("잘못된 입력입니다. (서로 다른 3자리 숫자만 입력)")
            continue

        count += 1
        result = check_input(answer, user_input)
        print("=== 결과 ===")

        if result["strike"] == 3:
            print(f"정답입니다! ({answer}) 시도 횟수: {count}")
            break
        elif result["strike"] == 0 and result["ball"] == 0:
            print("Out !!!")
        else:
            print(f"Strike: {result['strike']} / Ball: {result['ball']}")


if __name__ == "__main__":
    play_game()
