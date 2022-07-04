
const_input = int(input('enter an integer: '))
exp_input = int(input('enter an integer: '))


def quadratic(c, n):
    counter = 0
    for _ in range(c):
        for _ in range(n):
            counter += 1
            print(counter)


if __name__ == "__main__":
    quadratic(const_input, exp_input)
