import itertools
import copy
from _intcode_computer import Computer

prx = Computer.parse_intcode_program("input.txt")

class AmpException(Exception):
    def __init__(self):
        pass

class Amp():
    def __init__(self, program):
        self._first_in = True
        p = copy.deepcopy(program)
        self._computer = Computer(p, self.on_in, self.on_out)

    def process(self, phase, input):
        self._input = input
        self._phase = phase
        if self._computer.run():
            raise AmpException
        return self._output

    def on_in(self):
        if self._first_in:
            self._first_in = False
            return self._phase
        else:
            return self._input

    def on_out(self, output):
        self._output = output


phase_settings = list(itertools.permutations([5,6,7,8,9]))

best_setting = None 
max_signal = 0
for phase_setting in phase_settings:
    signal = 0
    amps = [Amp(prx) for i in range(0,5)]
    print("current phase setting: " + str(phase_setting))
    idx = 0
    while True:
        ps = phase_setting[idx]
        amp = amps[idx]
        try:
            signal = amp.process(ps, signal)
        except AmpException:
            break
        idx = (idx + 1) % 5
    if signal > max_signal:
        max_signal = signal
        best_setting = phase_setting


print("Max signal is %i for phase setting "%max_signal + str(best_setting))
    