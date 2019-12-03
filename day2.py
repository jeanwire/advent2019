
def main():
    i = 0
    with open('input_day_2.txt') as f:
        input = f.readline().strip().split(',')
        input = [int(i) for i in input]

        while i < len(input) - 3:
            if input[i] == 99:
                break

            pos1 = input[i + 1]
            pos2 = input[i + 2]
            pos3 = input[i + 3]

            if input[i] == 1:
                input[pos3] = input[pos1] + input[pos2]
            elif input[i] == 2:
                input[pos3] = input[pos1] * input[pos2]

            i += 4

    print(input)


if __name__ == '__main__':
    main()
