
def read_input():
    with open("input.txt") as f:
        first_line =  f.readlines()[0].split(",")
        return [int(i) for i in first_line]

program = read_input()

'''
Restore gravity assist program
'''
program[1] = 12
program[2] = 2

class Computer():
    def __init__(self, program):
        self.program = program
        self.pc = 0

    def run_operation(self):
        if self.program[self.pc] == 1: # add
            self.operation_add(self.program[self.pc+1], self.program[self.pc+2], self.program[self.pc+3])
            self.pc += 4

        elif self.program[self.pc] == 2: # multiply
            self.operation_mul(self.program[self.pc+1], self.program[self.pc+2], self.program[self.pc+3] )
            self.pc += 4
        
        elif self.program[self.pc] == 99: # end
            self.operation_end()

        else: # unknown oself.pcode
            print("PROGRAM ERROR, self.pc is %d!!!"%self.pc)
            exit()

    def operation_add(self, idx_a, idx_b, idx_result):
        self.program[idx_result] = self.program[idx_a] + self.program[idx_b]

    def operation_mul(self, idx_a, idx_b, idx_result):
        self.program[idx_result] = self.program[idx_a] * self.program[idx_b]

    def operation_end(self):
        print("Program ended, self.pc is %d."%self.pc)
        print("Value at position 0 is %d."%self.program[0])
        exit()

computer = Computer(program)
while True:
    computer.run_operation()