import random


def generate_number():
    numbers = []
    while len(numbers) < 6:
        n = random.randint(1, 45)
        if n not in numbers:
            numbers.append(n)
    numbers.sort()
    return numbers


if __name__ == "__main__":
    numbers = generate_number()
    print(numbers)
