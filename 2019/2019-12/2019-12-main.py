
class Moon():
    def __init__(self, x, y, z, name):
        self.cords = [x, y, z]
        self.vels = [0, 0, 0]
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

moons = read_input()
for t in range(0, 1000):
    processed_moons = 1
    for m1 in moons[:-1]:
        for m2 in moons[processed_moons:]:
            m1.apply_gravity_to_this_and_other_moon(m2)
        processed_moons += 1 
    for m in moons:
        m.apply_velocity()

total_energy = sum([m.get_kinetic_energy() * m.get_potential_energy() for m in moons])
print("Total energy in the Jupiter moons system is %d"%total_energy)