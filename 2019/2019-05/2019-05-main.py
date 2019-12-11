
def read_input():
    with open("input.txt") as f:
        first_line =  f.readlines()[0].split(",")
        return [int(i) for i in first_line]

program = read_input()
orig_prog = program[:]

ADD = 1
MUL = 2
MOV = 3
OUT = 4
END = 99


class InstructionFactory():
    def __init__(self):
        pass

    def get_instruction(self, program, pc):
        inst_code = program[pc] % 100
        if inst_code == ADD:
            return Add()
        elif inst_code == MUL:
            return Mul()
        elif inst_code == MOV:
            return Mov()
        elif inst_code == OUT:
            return Out()
        elif inst_code == END:
            return End()
        else:
            raise Exception()


class Instruction():
    def __init__(self, length):
        self._length = length

    def get_num_par(self):
        return self._length - 1

    def set_args(self, par_modes, pc, program):
        if len(par_modes) != self.get_num_par():
            raise Exception
        params = program[pc + 1 : pc + 1 + self.get_num_par()]
        self._args = [Argument(par, par_mode) for par, par_mode in zip(params, par_modes)]


class Add(Instruction):
    def __init__(self):
        super().__init__(4)
    
    def execute(self):
        self._args[2].set_val(self._args[0].get_val() + self._args[1].get_val())
 
 


class Mul(Instruction):
    def __init__(self):
        super().__init__(4)
    
    def execute(self):
        self._args[2].set_val(self._args[0].get_val() * self._args[1].get_val())


class Mov(Instruction):
    def __init__(self):
        super().__init__(2)
    
    def execute(self):
        value = int(input("Enter a number:"))
        self._args[0].set_val(value)


class Out(Instruction):
    def __init__(self):
        super().__init__(2)
    
    def execute(self):
        print("Out: %d"%(self._args[0].get_val()))
        
        
class End(Instruction):
    def __init__(self):
        super().__init__(1)
    
    def execute(self):
       print("Program executed.") 
       raise Exception


class Argument():
    def __init__(self, param, par_mode):
        self._param = param
        self._par_mode = par_mode

    def get_val(self):
        return self._par_mode.get_value(self._param)
    
    def set_val(self, val):
        self._par_mode.set_value(self._param, val)
          

class ParameterModeFactory():
    def __init__(self, program):
        self.program = program

    def get_par_mode(self, opcode_figure):
        if opcode_figure == 0:
            return PositionMode(self.program)
        elif opcode_figure == 1:
            return ImmediateMode(self.program)
        else:
            raise Exception()


class ParameterMode():
    def __init__(self, program):
        self._program = program
    

class PositionMode(ParameterMode):
    def __init__(self, program):
        super().__init__(program)

    def get_value(self, byte):
        return self._program[byte]

    def set_value(self, byte, val):
        self._program[byte] = val


class ImmediateMode(ParameterMode):
    def __init__(self, program):
        super().__init__(program)
    
    def get_value(self, byte):
        return byte
    
    def set_value(self, byte, val):
        raise Exception


class Computer():
    def __init__(self, program):
        self.program = program
        self.pc = 0
        self.inst_factory = InstructionFactory()
        self.par_mode_factory = ParameterModeFactory(program)
        
    def operand(self, operand_num):
        return self.program[self.pc + operand_num]
    
    def parse_opcode(self):
        raw = self.program[self.pc]
        instruction = self.inst_factory.get_instruction(self.program, self.pc)        
        num = instruction.get_num_par()
        par_codes = [int(i) for i in list(str(raw)[:-2])]
        par_codes.reverse()
        cur_len = len(par_codes)
        par_codes.extend([0] * (num - cur_len))
        par_modes = [self.par_mode_factory.get_par_mode(p_code) for p_code in par_codes]
        instruction.set_args(par_modes, self.pc, self.program)
        return (instruction, num + 1)

    def run(self):
        while True:
            instruction, length = self.parse_opcode()
            instruction.execute()
            self.pc += length

computer = Computer(program)
computer.run()
print("Diagnostic code is the last value on output.")