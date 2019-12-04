import math

def read_input():
    with open("input.txt") as f:
        lines = f.readlines()
        return (lines[0].split(','), lines[1].split(','))
    return

(cable, wire) = read_input()
print(str(cable))
print(str(wire))

def get_dir_and_len(direction_str):
   return (direction_str[0], int(direction_str[1:])) 

def get_lengths(cord):
    L = len(cord)
    even = L % 2 == 0
    if even:
        return (L/2, L/2)
    else:
       if (cord[0][0] in "UD"):
           return (math.floor(L/2) + 1, math.floor(L/2))
       else:
           return (math.floor(L/2), math.floor(L/2) +1)
    
def get_segments(cord, v_len, h_len):
    verts = []
    horiz = []
    v = 0
    h = 0
    for c in cord:
        direction, lenght = get_dir_and_len(c)
        if direction == "U":
            verts.append((h, (v, v + lenght)))
            v += lenght
        elif direction = "D":
            verts.append((h, (v - lenght, v)))
            v -= lenght
        elif direction = "R":
            horiz.append(((h, h + lenght), v))
            h += lenght
        else:
            horiz.append(((h - lenght, h), v))
            h -= lenght
    return (verts, horiz)


        

v_cables = []
h_cables = []
v_wires = []
h_wires = []
v_cables_len, h_cables_len = get_lengths(cable)
v_wires_len, h_wires_len = get_lengths(wire)
        

