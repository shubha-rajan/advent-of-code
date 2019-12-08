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
        # Opcode 1: Addition
        if opcode == 1:
            num1 = ints[pos + 1]
            num2 = ints[pos + 2]
            index = ints[pos + 3]
            if param_codes[0] == "0":
                num1 = ints[num1]
            if param_codes[1] == "0":
                num2 = ints[num2]
            ints[index] = num1 + num2
            pos += 4
        # Opcode 2: Multiplication
        elif opcode == 2:
            num1 = ints[pos + 1]
            num2 = ints[pos + 2]
            index = ints[pos + 3]
            if not int(param_codes[0]):
                num1 = ints[num1]
            if not int(param_codes[1]):
                num2 = ints[num2]
            ints[index] = num1 * num2
            pos += 4
        # Opcode 3: Store value
        elif opcode == 3:
            num = input("Enter a value:")
            index = ints[pos + 1]
            ints[index] = int(num)
            pos += 2
        # Opcode 4: Print value
        elif opcode == 4:
            value = ints[pos + 1]
            if not int(param_codes[0]):
                print(ints[value])
            else: 
                print(value)
            pos += 2
        # Opcode 5: Jump if true
        elif opcode == 5:
            num1 = ints[pos + 1]
            num2 = ints[pos + 2]
            if not int(param_codes[0]):
                num1 = ints[num1]
            if not int(param_codes[1]):
                num2 = ints[num2]
            if num1: 
                pos = num2
            else: 
                pos += 3
        # Opcode 6: Jump if false
        elif opcode == 6:
            num1 = ints[pos + 1]
            num2 = ints[pos + 2]
            if not int(param_codes[0]):
                num1 = ints[num1]
            if not int(param_codes[1]):
                num2 = ints[num2]
            if not num1: 
                pos = num2
            else: 
                pos += 3
        # Opcode 7: Less than
        elif opcode == 7:
            num1 = ints[pos + 1]
            num2 = ints[pos + 2]
            index = ints[pos + 3]
            if not int(param_codes[0]):
                num1 = ints[num1]
            if not int(param_codes[1]):
                num2 = ints[num2]
            if num1 < num2: 
                ints[index] = 1
            else: 
                ints[index] = 0
            pos += 4
        # Opcode 8: Equals
        elif opcode == 8:
            num1 = ints[pos + 1]
            num2 = ints[pos + 2]
            index = ints[pos + 3]
            if not int(param_codes[0]):
                num1 = ints[num1]
            if not int(param_codes[1]):
                num2 = ints[num2]
            if num1 == num2: 
                ints[index] = 1
            else: 
                ints[index] = 0
            pos += 4
    return ints

if __name__ == "__main__":
    ints = readnums()
    print(intcode(ints))