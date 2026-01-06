def algorithm(inputs, target):
    left = 0
    right = len(inputs) - 1
    while left <= right:
        mid = (left + right) // 2
        print(mid)
        if inputs[mid] == target:
            return mid
        elif inputs[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    inputs = [1, 2, 5, 7, 10, 20]
    result = algorithm(inputs, 2)
    print(f"result: {result}")
