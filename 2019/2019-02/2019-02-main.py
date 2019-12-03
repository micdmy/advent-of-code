
def read_input():
    with open("input.txt") as f:
        first_line =  f.readlines()[0].split(",")
        return [int(i) for i in first_line]

program = read_input()
orig_prog = program[:]


'''
Restore gravity assist program
'''
program[1] = 13
program[2] = 2

class Computer():
    def __init__(self, pogram):
        self.program = pogram
        self.pc = 0
        self.vars = []
        self.opers = []
        

    def run_operation(self):
        if self.program[self.pc] == 1: # add
            self.operation_add(self.program[self.pc+1], self.program[self.pc+2], self.program[self.pc+3])
            self.pc += 4
            self.vars.append(self.program[self.pc+3])
            self.opers.append(Add(self.program[self.pc+1], self.program[self.pc+2], self.program[self.pc+3]))

        elif self.program[self.pc] == 2: # multiply
            self.operation_mul(self.program[self.pc+1], self.program[self.pc+2], self.program[self.pc+3] )
            self.pc += 4
            self.vars.append(self.program[self.pc+3])
            self.opers.append(Mul(self.program[self.pc+1], self.program[self.pc+2], self.program[self.pc+3]))
        
        elif self.program[self.pc] == 99: # end
            self.operation_end()

        else: # unknown oself.pcode
            print("PROGRAM ERROR, self.pc is %d!!!"%self.pc)
            raise KeyboardInterrupt

    def operation_add(self, idx_a, idx_b, idx_result):
        self.program[idx_result] = self.program[idx_a] + self.program[idx_b]

    def operation_mul(self, idx_a, idx_b, idx_result):
        self.program[idx_result] = self.program[idx_a] * self.program[idx_b]

    def operation_end(self):
        print("Program ended, self.pc is %d."%self.pc)
        print("Value at position 0 is %d."%self.program[0])
        raise KeyboardInterrupt

class Oper:
    def __init__(self, idx_a, idx_b, idx_result):
        self.idx_a = idx_a
        self.idx_b = idx_b
        self.idx_result = idx_result
        self.val_a = None
        self.val_b = None
        
    def __str__(self):
        return "%d = %d %s %d [%d]"%(self.idx_result, self.idx_a, self.char, self.idx_b, self.val_b if self.val_b else "")

    def make_constant(self, constant_idx, value):
        if constant_idx == self.idx_a:
            if self.val_b:
                self.val_a = self.val_b
            self.idx_a = self.idx_b
            self.idx_b = constant_idx
            self.val_b = value
        elif constant_idx == self.idx_b:
            self.val_b = value


class Mul(Oper):
    def __init__(self, idx_a, idx_b, idx_result):
        super().__init__(idx_a, idx_b, idx_result)
        self.char = "*"
    
    def get_mul(self):
        return self.val_b

    def get_sum(self):
        return 0
        
class Add(Oper):
    def __init__(self, idx_a, idx_b, idx_result):
        super().__init__(idx_a, idx_b, idx_result)
        self.char = "+"

    def get_mul(self):
        return 1

    def get_sum(self):
        return self.val_b

computer = Computer(program)
try:
    while True:
        computer.run_operation()
except KeyboardInterrupt:
    pass
            
var_idxs = computer.vars
max_var_idx = max(var_idxs)
con_idxs = [i for i in range(0, max_var_idx+1) if i not in var_idxs]

opers = computer.opers

for c in con_idxs:
    for op in opers:
        op.make_constant(c, program[c])

for o in opers:
    print(o)

rev = opers[4:-1]
rev.reverse()

main_sum = 0
multiplier = 1
sumator = 0
expected = 19690720
for r in rev:
    if r.char == "+":
        main_sum += multiplier * r.get_sum()
    elif r.char == "*":
        multiplier *= r.get_mul()

print("%d = %d + (%d * x)"%(expected, main_sum, multiplier))
val19 = (expected - main_sum) / multiplier
print("Under adr 19 there is %d"%val19)
val1 = val19 - program[13]
print("val1 = %d"%val1)

for k in range(0,100):
    for m in range(0,100):
        pr = orig_prog[:]
        pr[1] = k
        pr[2] = m
        comp = Computer(pr)
        try:
            while True:
                comp.run_operation()
        except KeyboardInterrupt:
            pass
        if pr[0] == expected:
            print("Hurra k=%d, m=%d"%(k, m))
            exit()