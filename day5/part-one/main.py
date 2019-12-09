OPCODE_JUMPS = {
    1:4, 2:4, 3:2, 4:2,
}

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
        inst = str(ints[pos])
        opcode = int(inst[-2:])
        param_codes = list(inst[-3::-1])
        while len(param_codes) < 3:
            param_codes += ["0"]
        
        num1 = ints[pos + 1]
        num2 = ints[pos + 2]
        num3 = ints[pos + 3]

        # Opcode 1: Addition
        if opcode == 1:
            if not int(param_codes[0]):
                num1 = ints[num1]
            if not int(param_codes[1]):
                num2 = ints[num2]
            ints[num3] = num1 + num2
        # Opcode 2: Multiplication
        elif opcode == 2:
            if not int(param_codes[0]):
                num1 = ints[num1]
            if not int(param_codes[1]):
                num2 = ints[num2]
            ints[num3] = num1 * num2
        # Opcode 3: Store value
        elif opcode == 3:
            num = input("Enter a value:")
            ints[ints[pos+1]] = int(num)
        # Opcode 4: Print value
        elif opcode == 4:
            if not int(param_codes[0]):
                num1 = ints[num1]
            print(num1)
        pos += OPCODE_JUMPS[opcode]
    return ints

if __name__ == "__main__":
    ints = readnums()
    print(intcode(ints))