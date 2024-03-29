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
        self.instr = None
        self.opcode = None
        self.param_codes = None
        self.output = None
        self.halted = False

    def queue_input(self, input):
        self.inputs.append(input)
    
    def add(self, num1, num2, num3):
        if not int(self.param_codes[0]):
            num1 = self.ints[num1]
        if not int(self.param_codes[1]):
            num2 = self.ints[num2]
        self.ints[num3] = num1 + num2
    
    def multiply(self, num1, num2, num3):
        if not int(self.param_codes[0]):
            num1 = self.ints[num1]
        if not int(self.param_codes[1]):
            num2 = self.ints[num2]
        self.ints[num3] = num1 * num2
    
    def store(self):
        if self.inputs:
            num = self.inputs.pop()
            self.ints[ints[self.pos+1]] = int(num)
    
    def set_output(self, num1):
        if not int(self.param_codes[0]):
            num1 = self.ints[num1]
        self.output = num1

    def jump_if_true(self, num1, num2, num3):
        if not int(self.param_codes[0]):
            num1 = self.ints[num1]
        if not int(self.param_codes[1]):
            num2 = self.ints[num2]
        if num1: 
            self.pos = num2
            return True
        return False

    def jump_if_false(self, num1, num2, num3):
        if not int(self.param_codes[0]):
            num1 = self.ints[num1]
        if not int(self.param_codes[1]):
            num2 = self.ints[num2]
        if not num1: 
            self.pos = num2
            return True
        return True

    def less_than(self, num1, num2, num3):
        if not int(self.param_codes[0]):
            num1 = self.ints[num1]
        if not int(self.param_codes[1]):
            num2 = self.ints[num2]
        if num1 < num2: 
            self.ints[num3] = 1
        else: 
            self.ints[num3] = 0
    
    def equals(self, num1, num2, num3):
        if not int(self.param_codes[0]):
            num1 = self.ints[num1]
        if not int(self.param_codes[1]):
            num2 = self.ints[num2]
        if num1 == num2: 
            self.ints[num3] = 1
        else: 
            self.ints[num3] = 0

    def intcode(self):
        while self.ints[self.pos] != 99:  
            self.instr = str(self.ints[self.pos])
            self.opcode = int(self.instr[-2:])
            self.param_codes = list(self.instr[-3::-1])
            while len(self.param_codes) < 3:
                self.param_codes += ["0"]
            
            num1 = self.ints[self.pos + 1]
            num2 = self.ints[self.pos + 2]
            num3 = self.ints[self.pos + 3]

            if self.opcode == 1: self.add(num1, num2, num3)
            elif self.opcode == 2: self.multiply(num1, num2, num3)
            elif self.opcode == 3: 
                 if self.inputs: self.store() 
                 else: return
            elif self.opcode == 4: self.set_output(num1)
            elif self.opcode == 5: 
                if self.jump_if_true(num1, num2, num3): continue
            elif self.opcode == 6: 
                if self.jump_if_false(num1, num2, num3): continue
            elif self.opcode == 7: self.less_than(num1, num2, num3)
            elif self.opcode == 8: self.equals(num1, num2, num3)
                
            self.pos += OPCODE_JUMPS[self.opcode]
        self.halted= True


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
