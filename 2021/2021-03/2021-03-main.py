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

def count_mcb(lines):
    L = len(lines[1])
    N = len(lines)
    bit_counter = [0 for x in range(0, L)]

    for line in lines:
        bits = parse_bits(line)
        bit_counter = [bit_counter[i] + bits[i] for i in range(0, L)]

    MCB = []
    for cnt in bit_counter:
        if cnt >= N / 2:
            MCB.append("1")
        elif cnt < N / 2:
            MCB.append("0")
    return MCB

MCB = count_mcb(lines)

most_common_bits = int("".join(MCB), base=2)
least_common_bits = (pow(2, L)-1) ^ most_common_bits
LCB = ["1" if b == "0" else "0" for b in MCB]
print("MCB = {0:2}".format(most_common_bits))
print("LCB = {0:2}".format(least_common_bits))
print("Answer part 1 = {}".format(most_common_bits * least_common_bits))


lines_copy = lines
for i in range(0, L):
    lines = [line for line in lines if line[i] == MCB[i]]    
    if len(lines) == 1:
        break
    MCB = count_mcb(lines)

ogr = int(lines[0], base=2)

lines = lines_copy
for i in range(0, L):
    lines = [line for line in lines if line[i] == LCB[i]]    
    if len(lines) == 1:
        break
    mcb = count_mcb(lines)
    LCB = ["1" if b == "0" else "0" for b in mcb]

csr = int(lines[0], base=2)

print("ogr= {} csr= {} , multiplied = {}".format(ogr, csr, csr * ogr))
