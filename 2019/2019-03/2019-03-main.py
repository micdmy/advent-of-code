import math

def read_input():
    with open("input.txt") as f:
        lines = f.readlines()
        return (lines[0].split(','), lines[1].split(','))
    return

(cable, wire) = read_input()

def get_dir_and_len(direction_str):
   return (direction_str[0], int(direction_str[1:])) 

# def get_lengths(cord):
#     L = len(cord)
#     even = L % 2 == 0
#     if even:
#         return (L/2, L/2)
#     else:
#        if (cord[0][0] in "UD"):
#            return (math.floor(L/2) + 1, math.floor(L/2))
#        else:
#            return (math.floor(L/2), math.floor(L/2) +1)
    
def get_segments(cord):
    verts = []
    horiz = []
    v = 0
    h = 0
    for c in cord:
        direction, lenght = get_dir_and_len(c)
        if direction == "U":
            verts.append((h, (v, v + lenght)))
            v += lenght
        elif direction == "D":
            verts.append((h, (v - lenght, v)))
            v -= lenght
        elif direction == "R":
            horiz.append(((h, h + lenght), v))
            h += lenght
        else:
            horiz.append(((h - lenght, h), v))
            h -= lenght
    return (verts, horiz)

def find_closest_crossing(v_cords, h_cords):
    min_dist = float("inf")
    for vc in v_cords:
        for hc in h_cords:
            if hc[0][0] <= vc[0] <= hc[0][1]:
                if vc[1][0] <= hc[1] <= vc[1][1]:
                    dist = abs(vc[0]) + abs(hc[1])
                    if min_dist > dist:
                        min_dist = dist
    return min_dist
        
(v_cables_seg, h_cables_seg) = get_segments(cable)
(v_wires_seg, h_wires_seg) = get_segments(wire)

min1 = find_closest_crossing(v_cables_seg, h_wires_seg)
min2 = find_closest_crossing(v_wires_seg, h_cables_seg)

print("Closest intersetcion to central port has manhattan distance of %d to the central port."%min([min1, min2]))
