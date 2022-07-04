
user_input = int(input('input an integer: '))


def quadratic(n):
    i = 1
    step = 0
    while i < n:
        step += 1
        print(f'{step}:{i}')
        i = i * 2


if __name__ == "__main__":
    quadratic(user_input)
