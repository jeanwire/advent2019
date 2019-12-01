def main():
    fuel_total = 0
    with open('input_day_1.txt') as f:
        modules = f.readlines()
        for i in modules:
            module_fuel = int(i) // 3 - 2
            fuel_total += module_fuel
            while module_fuel > 0:
                module_fuel = module_fuel // 3 - 2
                if module_fuel > 0:
                    fuel_total += module_fuel

    print(fuel_total)


if __name__ == '__main__':
    main()
