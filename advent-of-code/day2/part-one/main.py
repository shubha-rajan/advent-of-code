
def readnums():
    ints = []
    with open("../input.txt") as f:
        for line in f:
            for num in line.split(","):
                ints.append(int(num))
    ints[1] = 12
    ints[2] = 2
    return ints

def intcode(ints):
    pos = 0
    
    while ints[pos] != 99:
        if ints[pos] == 1:
            num1 = ints[pos + 1]
            num2 = ints[pos + 2]
            index = ints[pos + 3]
            ints[index] = ints[num1] + ints[num2]
        elif ints[pos] == 2:
            num1 = ints[pos + 1]
            num2 = ints[pos + 2]
            index = ints[pos + 3]
            ints[index] = ints[num1] * ints[num2]
        pos += 4
    
    return ints

if __name__ == "__main__":
    print(intcode(readnums()))
    