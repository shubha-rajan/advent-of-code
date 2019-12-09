from itertools import permutations
from collections import deque
OPCODE_JUMPS = {
    1:4, 2:4, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4
}

def readnums():
    ints = []
    with open("../input.txt") as f:
        for line in f:
            for num in line.split(","):
                ints.append(int(num))
    return ints

class Computer():
    def __init__(self, ints, inputs):
        self.ints = ints
        self.inputs = deque(inputs)
        self.pos = 0
        self.output = None


    def intcode(self):
        while self.ints[self.pos] != 99:  
            inst = str(self.ints[self.pos])
            opcode = int(inst[-2:])
            param_codes = list(inst[-3::-1])
            while len(param_codes) < 3:
                param_codes += ["0"]
            
            num1 = self.ints[self.pos + 1]
            num2 = self.ints[self.pos + 2]
            num3 = self.ints[self.pos + 3]

            # Opcode 1: Addition
            if opcode == 1:
                if not int(param_codes[0]):
                    num1 = self.ints[num1]
                if not int(param_codes[1]):
                    num2 = self.ints[num2]
                self.ints[num3] = num1 + num2
            # Opcode 2: Multiplication
            elif opcode == 2:
                if not int(param_codes[0]):
                    num1 = self.ints[num1]
                if not int(param_codes[1]):
                    num2 = self.ints[num2]
                self.ints[num3] = num1 * num2
            # Opcode 3: Store value
            elif opcode == 3:
                if self.inputs:
                    num = self.inputs.pop()
                    self.ints[ints[self.pos+1]] = int(num)
                else:
                    break
            # Opcode 4: Print value
            elif opcode == 4:
                if not int(param_codes[0]):
                    num1 = self.ints[num1]
                self.output = num1
            # Opcode 5: Jump if true
            elif opcode == 5:
                if not int(param_codes[0]):
                    num1 = self.ints[num1]
                if not int(param_codes[1]):
                    num2 = self.ints[num2]
                if num1: 
                    self.pos = num2
                    continue
            # Opcode 6: Jump if false
            elif opcode == 6:
                if not int(param_codes[0]):
                    num1 = self.ints[num1]
                if not int(param_codes[1]):
                    num2 = self.ints[num2]
                if not num1: 
                    self.pos = num2
                    continue
            # Opcode 7: Less than
            elif opcode == 7:
                if not int(param_codes[0]):
                    num1 = self.ints[num1]
                if not int(param_codes[1]):
                    num2 = self.ints[num2]
                if num1 < num2: 
                    self.ints[num3] = 1
                else: 
                    self.ints[num3] = 0
            # Opcode 8: Equals
            elif opcode == 8:
                if not int(param_codes[0]):
                    num1 = self.ints[num1]
                if not int(param_codes[1]):
                    num2 = self.ints[num2]
                if num1 == num2: 
                    self.ints[num3] = 1
                else: 
                    self.ints[num3] = 0
            self.pos += OPCODE_JUMPS[opcode]


def max_signal(ints): 
    sequences = permutations(range(5))
    max_signal = float("-inf")
    
    for sequence in sequences:
        signal = 0
        for amp in sequence:
            comp = Computer(ints, [signal, amp])
            comp.intcode()
            signal = comp.output
        if signal > max_signal:
            max_signal = signal
    return max_signal



if __name__ == "__main__":
    ints = readnums()
    print(max_signal(ints))
