

def main():
    fuel_total = 0
    with open('input_day_1.txt') as f:
        modules = f.readlines()
        for i in modules:
            fuel_total += int(i) // 3 - 2

    print(fuel_total)


if __name__ == '__main__':
    main()
