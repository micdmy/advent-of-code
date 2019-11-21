
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
        


