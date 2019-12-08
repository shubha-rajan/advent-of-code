import math
def get_total_fuel():
    total = 0
    def add_fuel(mass):
        nonlocal total
        fuel = math.floor(mass/3) -2
        if fuel > 0:
            total += fuel
            add_fuel(fuel)

    with open('../input.txt') as f:
        for line in f:
            mass = int(line)
            add_fuel(mass)
    return total


if __name__ == "__main__":
    print(get_total_fuel())