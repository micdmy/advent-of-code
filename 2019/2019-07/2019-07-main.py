import itertools
import copy
from _intcode_computer import Computer

prx = Computer.parse_intcode_program("input.txt")


class Amp():
    def __init__(self):
        self._first_in = True
        pass

    def process(self, phase, input):
        self._input = input
        self._phase = phase
        p = copy.deepcopy(prx)
        computer = Computer(p, self.on_in, self.on_out)
        computer.run()
        return self._output

    def on_in(self):
        if self._first_in:
            self._first_in = False
            return self._phase
        else:
            return self._input

    def on_out(self, output):
        self._output = output


phase_settings = list(itertools.permutations([0,1,2,3,4]))

best_setting = None 
max_signal = 0
for phase_setting in phase_settings:
    signal = 0
    print("current phase setting: " + str(phase_setting))
    for ps in phase_setting:
        amp = Amp()
        signal = amp.process(ps, signal)
    if signal > max_signal:
        max_signal = signal
        best_setting = phase_setting


print("Max signal is %i for phase setting "%max_signal + str(best_setting))
    