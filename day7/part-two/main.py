from itertools import permutations, cycle
from collections import deque

OPCODE_JUMPS = {
    1:4, 2:4, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4
}

def readnums():
    ints = []
    with open("test.txt") as f:
        for line in f:
            for num in line.split(","):
                ints.append(int(num))
    return ints

class Computer():
    def __init__(self, ints, inputs, label):
        self.id = label
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

    def jump_if_true(self, num1, num2):
        if not int(self.param_codes[0]):
            num1 = self.ints[num1]
        if not int(self.param_codes[1]):
            num2 = self.ints[num2]
        if num1:
            self.pos = num2
        else:        
            self.pos += 3

    def jump_if_false(self, num1, num2):
        if not int(self.param_codes[0]):
            num1 = self.ints[num1]
        if not int(self.param_codes[1]):
            num2 = self.ints[num2]
        if not num1: 
            self.pos = num2
        else:        
            self.pos += 3

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
        print(self.id, self.pos, self.opcode)
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
                self.jump_if_true(num1, num2) 
                continue
            elif self.opcode == 6: 
                self.jump_if_false(num1, num2)
                continue
            elif self.opcode == 7: self.less_than(num1, num2, num3)
            elif self.opcode == 8: self.equals(num1, num2, num3)
                
            self.pos += OPCODE_JUMPS[self.opcode]
        self.halted= True



class FeedbackLoop():
    def __init__(self):
        self.sequences = permutations(range(5, 10))
        self.computers = []


    def initialize_computers(self, sequence):
        self.computers = []
        for i, phase in enumerate(sequence):
            comp = Computer(ints, [phase], i)
            self.computers.append(comp)
            comp.intcode()

    def loop(self, sequence):
        signal = 0
        while all([not comp.halted for comp in self.computers]):
            for computer in self.computers:
                computer.queue_input(signal)
                computer.intcode()
                signal = computer.output
                
        return signal
    
    def max_output(self):
        max_signal = float("-inf")
        for sequence in self.sequences:
            loop.initialize_computers(sequence)
            print(self.computers, max_signal)
            signal = self.loop(sequence)
            if signal > max_signal: max_signal = signal
        return max_signal



if __name__=="__main__":
    ints = readnums()
    loop = FeedbackLoop()
    print(loop.max_output())
