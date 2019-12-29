import keyboard as kb
import time
from collections import defaultdict

class Board():
    def __init__(self):
        self.tiles = [[""]]

    def set_tile(self,x, y, val):
        y += 1
        y_ext = y - len(self.tiles) + 1
        self.tiles.extend([[]] * y_ext)
        x_ext = x - len(self.tiles[y]) + 1
        self.tiles[y].extend([" "] * x_ext)
        self.tiles[y][x] = val

    def set_score(self, score):
        self.tiles[0] = "SCORE: %d"%score
    
    def __str__(self):
        ret_buf = ""
        for row in self.tiles:
            ret_buf = ret_buf + "".join(row) + "\n"
        return ret_buf
    
    def get_num_of(self, val):
        count = 0
        for row in self.tiles:
            for c in row:
                if c == val:
                    count += 1
        return count
            

class Game():
    tile_chars = [" ", "#", "*", "=", "o"]
    board = Board()
    def __init__(self):
        pass
    
    @classmethod
    def set_tile(cls, x, y, _type):
        if x == -1 and y == 0:
            cls.board.set_score(_type)
        else:
            if _type == 4:
                Joystick.set_ball(x)
            elif _type == 3:
                Joystick.set_pad(x)
            cls.board.set_tile(x, y, cls.tile_chars[_type])

    @classmethod
    def draw(cls):
        print(str(cls.board))
    
    @classmethod
    def get_first_part_result(cls):
        return cls.board.get_num_of("*")


class OutputObserver():
    current_order = [0,0,0]
    idx = 0
    def __init__(self):
        pass

    @classmethod
    def on_new_output(cls, output):
        cls.current_order[cls.idx] = output
        if cls.idx < 2:
            cls.idx += 1
        else:
            cls.idx = 0
            Game.set_tile(*cls.current_order)
            Game.draw()


class Joystick():
    ball_x = None
    pad_x = None

    def __init__(self):
        pass

    @classmethod
    def get_position(cls):
        if cls.ball_x == None or cls.pad_x == None:
            return 0
        if cls.ball_x > cls.pad_x:
            return 1
        elif cls.ball_x < cls.pad_x:
            return -1
        else:
            return 0

    @classmethod
    def set_ball(cls, ball_x):
        cls.ball_x = ball_x

    @classmethod
    def set_pad(cls, pad_x):
        cls.pad_x = pad_x

## INTCODE COMPUTER BEGIN
def read_input():
    with open("input.txt") as f:
        first_line =  f.readlines()[0].split(",")
        return [int(i) for i in first_line]

list_program = read_input()
program = defaultdict(int)

for i, instr in enumerate(list_program):
    program[i] = instr

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

class RelativeBase():
    value = 0

    def __init__(self):
        pass

    @classmethod
    def get(cls):
        return cls.value

    @classmethod
    def increment(cls, increment_by):
        cls.value += increment_by


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
        elif inst_code == JNZ:
            return Jnz()
        elif inst_code == JZ:
            return Jz()
        elif inst_code == LT:
            return Lt()
        elif inst_code == EQ:
            return Eq()
        elif inst_code == ARB:
            return Arb()
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
    def __init__(self):
        super().__init__(2)
    
    def execute(self):
        # value = int(input("Enter a number:"))
        value = Joystick.get_position()
        self._args[0].set_val(value)


class Out(Instruction):
    def __init__(self):
        super().__init__(2)
    
    def execute(self):
        # print("Out: %d"%(self._args[0].get_val()))
        OutputObserver.on_new_output(self._args[0].get_val())
        
        
class End(Instruction):
    def __init__(self):
        super().__init__(1)
    
    def execute(self):
        print("Solution of the fist part is %d"%Game.get_first_part_result())
        print("Program executed.") 
        raise Exception


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
    def __init__(self):
        super().__init__(2)
    
    def execute(self):
        RelativeBase.increment(self._args[0].get_val())


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
        elif opcode_figure == 2:
            return RelativeMode(self.program)
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
    def __init__(self, program):
        super().__init__(program)

    def get_value(self, byte):
        return self._program[byte + RelativeBase.get()]  

    def set_value(self, byte, val):
        self._program[byte + RelativeBase.get()] = val

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
            self.pc = instruction.get_new_pc_value(self.pc)
            # print("PC: %d"%self.pc)

# Hack the number of quearter put in the machine:
program[0] = 2

computer = Computer(program)
computer.run()