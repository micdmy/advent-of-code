
def read_input():
    with open("input.txt") as f:
        return [str(line) for line in f]

lines = read_input()

class Asteroid():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def angle_to(asteroid):


asteroids = []

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '#':
            asteroids.append(Asteroid(x, y))
