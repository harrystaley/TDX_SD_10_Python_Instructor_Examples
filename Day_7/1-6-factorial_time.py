
permute_list = [5, 6, 7, 8]


def permutations(lis):
    if len(lis) == 1:
        return [lis]

    output = []
    *front, last = lis

    for perm in permutations(front):
        for i in range(len(perm) + 1):
            new = perm[:i] + [last] + perm[i:]
            output.append(new)

    return sorted(output)


if __name__ == "__main__":
    lists = permutations(permute_list)
    counter = 1
    for item in lists:
        print(f"{counter}:{item}")
        counter += 1
