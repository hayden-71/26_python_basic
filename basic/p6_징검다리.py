stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
cnt = 0


# left = 1
# right = len(stones)

# # while문 사용

# while left <= right:  # 뒤에 오는 조건이 참일때만 돌아간다
#     mid = (left + right) % 2
#     for stone in stones:
#         stone -= 1
#     cnt += 1

# def solution(stones, k):
#     answer = 0
#     return answer


def solution(stones, k):
    answer = 0
    possible = True

    while possible:
        idx = 0
        while idx <= len(stones) - 1 and possible:
            if stones[idx] > 0:
                stones[idx] -= 1
                idx += 1
            else:
                jump = False
                for i in range(idx + 1, idx + k):
                    if i >= len(stones):
                        idx = len(stones)
                        break
                    if stones[i] != 0:
                        idx = i
                        jump = True
                        break

                if jump == False:
                    if idx != len(stones):
                        possible = False

        if possible:
            answer += 1

    return answer


# k구간에서 최댓값끼리 비교했을 때, 최솟값이 건널 수 있는 수
def solution2(stones, k):
    answer = 0
    max_numbers = []

    for i in range(0, len(stones) - k + 1):
        m = max(stones[i : i + k])
        max_numbers.append(m)
    return min(max_numbers)


print(solution2(stones, k))


# binary search
def solution3(stones, k):
    left = 0
    right = max(stones)
    answer = 0

    while left <= right:
        mid = (left + right) // 2  # 건널 수 있는지 테스트해보자
        count = 0
        possible = True

        for s in stones:
            if s < mid:  # 돌에 적힌 숫자가, 건너는 사람보다 작다면? 돌이 못 버티면 +1
                count += 1  # 돌이 사라진 수 카운트
                if count == k:
                    possible = False  # 못 건너니까 그만둬
                    break
            else:
                count = 0

        if possible:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
    return answer
