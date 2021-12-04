import logging
def read_input():
    with open("input.txt") as f:
        return [str(line)[:-1] for line in f]
    return

def parse_bits(string_with_bits):
    return [int(b) for b in string_with_bits]
lines = read_input()
L = len(lines[1])
N = len(lines)
bit_counter = [0 for x in range(0, L)]

for line in read_input():
    bits = parse_bits(line)
    bit_counter = [bit_counter[i] + bits[i] for i in range(0, L)]

MCB = []
for cnt in bit_counter:
    if cnt > N / 2:
        MCB.append("1")
    elif cnt < N / 2:
        MCB.append("0")
    else:
        logging.error("The same number of 0 and 1 bits")

most_common_bits = int("".join(MCB), base=2)
least_common_bits = (pow(2,12)-1) ^ most_common_bits
print("MCB = {0:2}".format(most_common_bits))
print("LCB = {0:2}".format(least_common_bits))
print("Answer part 1 = {}".format(most_common_bits * least_common_bits))