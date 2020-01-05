import math

def read_input():
    with open("input.txt") as f:
        return [str(line) for line in f]

lines = read_input()

class Asteroid():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visible = {}

    def angle_to(self, asteroid):
        return math.atan2(asteroid.x - self.x, asteroid.y - self.y)

    def add_visible(self, asteroid, angle):
        self.visible[angle] = asteroid


asteroids = []

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '#':
            asteroids.append(Asteroid(x, y))

for counter, asteroid in enumerate(asteroids):
    print("Counter: %d"%counter)
    for other_asteroid in asteroids:
        if other_asteroid is not asteroid:
            angle = asteroid.angle_to(other_asteroid)
            asteroid.add_visible(other_asteroid, angle)

max_visible_cnt = 0
best_asteroid = None
for asteroid in asteroids:
    if len(asteroid.visible) > max_visible_cnt:
        max_visible_cnt = len(asteroid.visible)
        best_asteroid = asteroid

print("Best asteroid for station is: x = %i, y = %i, cnt = %i"%(best_asteroid.x, best_asteroid.y, len(best_asteroid.visible)))

