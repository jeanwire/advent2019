
def main():
    with open('input_day_2.txt') as f:
        program = f.readline().strip().split(',')
        program = [int(i) for i in program]

        solved = False

        for j in range(0,100):
            for k in range(0,100):
                input = program.copy()
                i = 0
                input[1] = j
                input[2] = k

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

                if input[0] == 19690720:
                    solved = True
                    print('SOLVED: ' , j, ' ', k)

            if solved:
                break


if __name__ == '__main__':
    main()
