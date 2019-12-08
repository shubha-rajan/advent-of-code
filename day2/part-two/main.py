def readnums():
    ints = []
    with open("../input.txt") as f:
        for line in f:
            for num in line.split(","):
                ints.append(int(num))
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

def find_noun_and_verb():
    for i in range(100):
        for j in range(100):
            ints = readnums()
            ints[1] = i
            ints[2] = j
            if intcode(ints)[0] == 19690720: return (i, j)

if __name__ == "__main__":
    noun, verb = find_noun_and_verb()
    print(100 * noun + verb)
    