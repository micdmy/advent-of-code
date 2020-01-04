from collections import defaultdict




ADD = 1
MUL = 2
MOV = 3
OUT = 4
JNZ = 5
JZ = 6
LT = 7
EQ = 8
ARB = 9
END = 99

RET_CODE_HALT = 1
RET_CODE_TERMINATE = 2

class RelativeBase():
    def __init__(self):
        self.value = 0
        pass

    def get(self):
        return self.value

    def increment(self, increment_by):
        self.value += increment_by


class InstructionFactory():
    def __init__(self):
        pass

    def get_instruction(self, program, pc, relative_base, on_in, on_out):
        inst_code = program[pc] % 100
        if inst_code == ADD:
            return Add()
        elif inst_code == MUL:
            return Mul()
        elif inst_code == MOV:
            return Mov(on_in)
        elif inst_code == OUT:
            return Out(on_out)
        elif inst_code == END:
            return End()
        elif inst_code == JNZ:
            return Jnz()
        elif inst_code == JZ:
            return Jz()
        elif inst_code == LT:
            return Lt()
        elif inst_code == EQ:
            return Eq()
        elif inst_code == ARB:
            return Arb(relative_base)
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
        pcs = range(pc + 1, pc + 1 + self.get_num_par())
        params = [program[p] for p in pcs]
        self._args = [Argument(par, par_mode) for par, par_mode in zip(params, par_modes)]
    
    def get_new_pc_value(self, pc):
        return pc + self._length


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
    def __init__(self, on_in):
        super().__init__(2)
        self._on_in = on_in
    
    def execute(self):
        value = self._on_in()
        assert value != None
        self._args[0].set_val(value)


class Out(Instruction):
    def __init__(self, on_out):
        super().__init__(2)
        self._on_out = on_out
    
    def execute(self):
        self._on_out(self._args[0].get_val())
        return RET_CODE_HALT
        
        
class End(Instruction):
    def __init__(self):
        super().__init__(1)
    
    def execute(self):
        print("Program executed.") 
        return RET_CODE_TERMINATE


class Jnz(Instruction):
    def __init__(self):
        super().__init__(3)
        self._new_pc = None
    
    def execute(self):
        if self._args[0].get_val() != 0:
            self._new_pc = self._args[1].get_val()
    
    def get_new_pc_value(self, pc):
        if self._new_pc != None:
            return self._new_pc
        else:
            return super().get_new_pc_value(pc)


class Jz(Jnz):
    def __init__(self):
        super().__init__()
    
    def execute(self):
        if self._args[0].get_val() == 0:
            self._new_pc = self._args[1].get_val()
        

class Lt(Instruction):
    def __init__(self):
        super().__init__(4)

    def execute(self):
        if(self._args[0].get_val() < self._args[1].get_val()):
            self._args[2].set_val(1)
        else:
            self._args[2].set_val(0)
            
    
class Eq(Instruction):
    def __init__(self):
        super().__init__(4)

    def execute(self):
        if(self._args[0].get_val() == self._args[1].get_val()):
            self._args[2].set_val(1)
        else:
            self._args[2].set_val(0)


class Arb(Instruction):
    def __init__(self, relative_base):
        super().__init__(2)
        self._relative_base = relative_base
    
    def execute(self):
        self._relative_base.increment(self._args[0].get_val())


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

    def get_par_mode(self, opcode_figure, relative_base):
        if opcode_figure == 0:
            return PositionMode(self.program)
        elif opcode_figure == 1:
            return ImmediateMode(self.program)
        elif opcode_figure == 2:
            return RelativeMode(self.program, relative_base)
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

class RelativeMode(ParameterMode):
    def __init__(self, program, relative_base):
        super().__init__(program)
        self._relative_base = relative_base

    def get_value(self, byte):
        return self._program[byte + self._relative_base.get()]  

    def set_value(self, byte, val):
        self._program[byte + self._relative_base.get()] = val

class Computer():
    def __init__(self, program, on_in, on_out):
        self.program = program
        self.pc = 0
        self.inst_factory = InstructionFactory()
        self.par_mode_factory = ParameterModeFactory(program)
        self.relative_base = RelativeBase()
        self.on_in = on_in
        self.on_out = on_out
        self.terminated = False
        
    def operand(self, operand_num):
        return self.program[self.pc + operand_num]
    
    def parse_opcode(self):
        raw = self.program[self.pc]
        instruction = self.inst_factory.get_instruction(self.program, self.pc, self.relative_base, self.on_in, self.on_out)        
        num = instruction.get_num_par()
        par_codes = [int(i) for i in list(str(raw)[:-2])]
        par_codes.reverse()
        cur_len = len(par_codes)
        par_codes.extend([0] * (num - cur_len))
        par_modes = [self.par_mode_factory.get_par_mode(p_code, self.relative_base) for p_code in par_codes]
        instruction.set_args(par_modes, self.pc, self.program)
        return (instruction, num + 1)

    def run(self):
        if self.terminated:
            return True
        while True:
            instruction, length = self.parse_opcode()
            ret_code = instruction.execute()
            self.pc = instruction.get_new_pc_value(self.pc)
            if ret_code == RET_CODE_HALT:
                return False
            elif ret_code == RET_CODE_TERMINATE:
                self.terminated = True
                return False

    @classmethod
    def parse_intcode_program(cls, file_name):
        with open(file_name) as f:
            first_line =  f.readlines()[0].split(",")
            list_program =  [int(i) for i in first_line]
            program = defaultdict(int)
            for i, instr in enumerate(list_program):
                program[i] = instr
            return program