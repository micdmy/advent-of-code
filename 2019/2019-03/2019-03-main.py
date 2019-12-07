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

class Segment():
    def __init__(self, pos, steps, begin):
        self.pos =  pos
        self.steps = steps    
        self.begin = begin

    def get_steps_to_crossing(self, coord):
        return self.steps + abs(coord - self.begin)


def get_segments(cord):
    verts = []
    horiz = []
    v = 0
    h = 0
    steps = 0
    for c in cord:
        direction, lenght = get_dir_and_len(c)
        if direction == "U":
            verts.append(Segment((h, (v, v + lenght)), steps, v))
            v += lenght
        elif direction == "D":
            verts.append(Segment((h, (v - lenght, v)), steps, v))
            v -= lenght
        elif direction == "R":
            horiz.append(Segment(((h, h + lenght), v), steps, h))
            h += lenght
        else:
            horiz.append(Segment(((h - lenght, h), v), steps, h))
            h -= lenght
        steps += lenght
    return (verts, horiz)

def are_crossed(v_seg, h_seg):
    vc = v_seg.pos
    hc = h_seg.pos
    return (hc[0][0] <= vc[0] <= hc[0][1]) and (vc[1][0] <= hc[1] <= vc[1][1])


def find_crossing(v_cords, h_cords):
    min_dist = float("inf")
    min_steps = float("inf")
    for vc_seg in v_cords:
        for hc_seg in h_cords:
            if are_crossed(vc_seg, hc_seg):
                dist = abs(vc_seg.pos[0]) + abs(hc_seg.pos[1])
                if min_dist > dist:
                    min_dist = dist
                steps = vc_seg.get_steps_to_crossing(hc_seg.pos[1]) + hc_seg.get_steps_to_crossing(vc_seg.pos[0])
                if min_steps > steps:
                    min_steps = steps
                
    return (min_dist, min_steps)

(v_cables_seg, h_cables_seg) = get_segments(cable)
(v_wires_seg, h_wires_seg) = get_segments(wire)

(min1, mstep1) = find_crossing(v_cables_seg, h_wires_seg)
(min2, mstep2) = find_crossing(v_wires_seg, h_cables_seg)

print("Closest intersetcion to central port has manhattan distance of %d to the central port."%min([min1, min2]))
print("The fewest combined steps the wires must take to reach an intersection is %d"%(min(mstep1, mstep2)))
