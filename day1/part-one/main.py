import math
def get_total_fuel():
    total = 0
    with open('../input.txt') as f:
        for line in f:
            mass = int(line)
            fuel = math.floor(mass/3) -2
            total += fuel
    return total

if __name__ == "__main__":
    print(get_total_fuel())