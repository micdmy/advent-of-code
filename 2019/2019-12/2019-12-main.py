from math import gcd
import numpy as np

class Moon():
    def __init__(self, x, y, z, name):
        self.cords = [x, y, z]
        self.vels = [0, 0, 0]
        self.orig_cords = [x, y, z]
        self.orig_vels = [0, 0, 0]
        self._name = name
    
    def apply_velocity(self):
        for i in range(0, 3):
            self.cords[i] += self.vels[i]

    def apply_gravity_to_this_and_other_moon(self, other_moon):
        for i in range(0, 3):
            if self.cords[i] > other_moon.cords[i]:
                self.vels[i] -= 1
                other_moon.vels[i] += 1
            elif self.cords[i] < other_moon.cords[i]:
                self.vels[i] += 1
                other_moon.vels[i] -= 1

    def get_potential_energy(self):
        a =  sum([abs(c) for c in self.cords])
        return a

    def get_kinetic_energy(self):
        a = sum([abs(v) for v in self.vels])
        return a
    
    def is_in_original_state(self):
        return self.cords == self.orig_cords and self.vels == self.orig_vels


def read_input():
    moons = []
    with open("input.txt") as f:
        names = ["Io", "Europa", "Ganymede", "Callisto"]
        name = iter(names)
        for line in f:
            parts = line.split()
            cords = [int("".join([c for c in p if c in "0123456789-"])) for p in parts]
            moons.append(Moon(*cords, next(name)))
    return moons

def grav(cs, vs, i, j):
    if cs[i] > cs[j]:
        vs[i] -= 1
        vs[j] += 1
    elif cs[i] < cs[j]:
        vs[i] += 1
        vs[j] -= 1
      


moons = read_input()

def repeats_for_one_coordinates(cords, look_for):
    xs_c = cords
    xs_v = [0,0,0,0]
    counter = 0
    while True:
        counter += 1
        grav(xs_c, xs_v, 0, 1)
        grav(xs_c, xs_v, 0, 2)
        grav(xs_c, xs_v, 0, 3)
        grav(xs_c, xs_v, 1, 3)
        grav(xs_c, xs_v, 1, 2)
        grav(xs_c, xs_v, 3, 2)
        xs_c = [c+v for c, v in zip(xs_c, xs_v)]
        if xs_v == [0,0,0,0] and xs_c == look_for:
            break
    return counter

rx = repeats_for_one_coordinates([m.cords[0] for m in moons], [m.cords[0] for m in moons])
ry = repeats_for_one_coordinates([m.cords[1] for m in moons], [m.cords[1] for m in moons])
rz = repeats_for_one_coordinates([m.cords[2] for m in moons], [m.cords[2] for m in moons])
print("repeats for x, y, z: %d %d %d"%(rx,ry,rz))

lcm = np.lcm.reduce([rx, ry, rz])
print("Universe is repeated itself after %d steps"%lcm)
    
'''
counter = 0
while True:
    counter += 1
    processed_moons = 1
    for m1 in moons[:-1]:
        for m2 in moons[processed_moons:]:
            m1.apply_gravity_to_this_and_other_moon(m2)
        processed_moons += 1 
    for m in moons:
        m.apply_velocity()
    if all([m.is_in_original_state() for m in moons]):
        print("Universe is repeated itself after %d steps"%counter)
    print(str(counter))
'''
total_energy = sum([m.get_kinetic_energy() * m.get_potential_energy() for m in moons])
print("Total energy in the Jupiter moons system is %d"%total_energy)

