
def read_input():
    with open("input.txt") as f:
        return [line.strip()+"" for line in f]
    return
lines = read_input()

s_lines = []
for line in lines:
    s_lines.append(sorted(line) + ["_"])

twos = 0
threes = 0
for line in s_lines:
    last_c = " "
    counter = 0
    two_found = False
    three_found = False
    for c in line:
        if c != last_c:
            if not two_found and counter == 1:
                twos += 1
                two_found = True
                if three_found:
                    break
            if not three_found and counter == 2:
                threes += 1
                three_found = True
                if two_found:
                    break
            counter = 0
        else:
            counter += 1
        last_c = c
        
print("PART 1: Twos: " + str(twos) + " Threes: " + str(threes) + " CHKSUM: " + str(twos*threes))
        
# PART TWO:

def remove_char_in_lines(pos, lines):
    return [l[:pos] + l[(pos+1):] for l in lines]


for rem_pos in range(0, len(lines[0])):
    print("rem_pos = " + str(rem_pos))
    lines_without_c = remove_char_in_lines(rem_pos, lines)
    for i in range(0, len(lines_without_c) - 1):
        if lines_without_c[i] in lines_without_c[i+1:]:
            print("PART 2: Found similar lines, index: " + str(i) + " equal chars: " + "".join(lines_without_c[i]))
            exit()

            

        