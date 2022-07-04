
user_input = int(input('How many times do you want to execute this loop?: '))


def linear(n):
    step = 0
    for _ in range(n):
        step += 1
        print(step)


if __name__ == "__main__":
    linear(user_input)
