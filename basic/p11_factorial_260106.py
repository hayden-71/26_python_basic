# 1. factorial 문제
# 5! = 5 x 4 x 3 x 2 x 1 = 120


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# 이렇게 쓸 수도 있음
# for i in range(n, 1, -1):


# while 사용하기
def fac(n):
    result = 1
    while n >= 2:  # 여기가 1이 아니라 2인 이유: 조금 더 효율적으로
        result *= n
        n -= 1  # 이거 안 쓰면 무한루프
    return result


# 재귀함수로 짜보기
def factorial2(n):
    # n = 5
    # 5 * factorial2(4)
    # 5 * 4 * factorial2(3)
    # 5 * 4 * 3 * factorial2(2)
    # 5 * 4 * 3 * 2 * 1
    if n <= 1:  # 멈추는 조건: n이 1이면 돌려줘
        return 1  # 마지막에 어떻게 끝날지가 있어야!
    else:
        return n * factorial2(n - 1)


print(f"5! = {factorial2(5)}")


# 2. 대칭 문자열
# level, aabbaa > True
# hello, abcd > False


def pa(s):
    for i in range(len(s) // 2):
        if s[i] != s[-1 - i]:
            return False  # 하나라도 예외 있으면/틀리면 탈락! 모두 맞아야만 함
    return True  # 결과적으로 True


# 뒤집어서 확인
def pa(s):
    return s == s[::-1]


# .pop() 사용하기
def pa(s):
    # s[0] vs s[-1]
    # s[1] vs s[-2]
    # s[2] vs s[-3]
    d = list(s)

    while len(d) > 1:
        first = d[0]
        del d[0]  # 혹은 이렇게 한줄로 first = s.pop(0)
        last = d.pop()
        if first != last:
            return False
    return True


# 재귀함수로 짜보기
# st[0] == st[-1]
# st[1:-1]
def ispalindrome(s):
    print(s)
    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        result = ispalindrome(s[1:-1])
        print(result)
        return result
    else:
        return False


ispalindrome("aaabbbaaa")

# 3. 문자열 대소문자 뒤집기
# abCdEfg >> ABcDeFG
# adC1@3 >> ABc!2#


def change_str(st):
    result = ""  # 비어있는 문자열

    # 쉬운 단축키
    st.swapcase()

    # 다른 방법
    result = "".join(
        [c.upper() if c.islower() else c.lower() for c in st]
    )  # 이건 뭐야.........

    # 다른 방법
    for s in st:
        if s.isupper():
            result += s.lower()
        else:
            result += s.upper()

    # 이렇게 구현 가능
    for s in st:
        if ord("A") <= ord(s) <= ord("Z"):  # 굳이 ord 안 써도 가능
            result += s.lower()
        elif ord("a") <= ord(s) <= ord("z"):
            result += s.upper()
