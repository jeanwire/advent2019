

def main():
    valid = 0
    for i in range(278384, 824796):
        if check_input(i):
            valid += 1

    print(valid)


def check_input(input):
    input = str(input)
    valid = False
    for i in range(5):
        if input[i] == input[i + 1]:
            valid = True
            break
    if not valid:
        return False
    for i in range(5):
        if input[i] > input[i + 1]:
            return False

    return True


if __name__ == '__main__':
    main()
