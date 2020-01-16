import math
from collections import defaultdict

def read_input():
    with open("input.txt") as f:
        return [str(line) for line in f]

lines = read_input()

class Asteroid():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visible = defaultdict(list)
        self.visible_sorted = []
        self.destruction_idx = None

    def __lt__(self, other):
        return self.distance < other.distance

    def __str__(self):
        return "X: %i, Y: %i"%(self.x, self.y)

    def angle_to(self, asteroid):
        return math.atan2(asteroid.x - self.x, asteroid.y - self.y)

    def count_distance(self, asteroid):
        xd = asteroid.x - self.x
        yd = asteroid.y - self.y
        self.distance = math.sqrt(math.pow(yd,2) + math.pow(xd,2))

    def add_visible(self, asteroid, angle):
        self.visible[angle].append(asteroid)
        
    def draw_map(self):
        Xlen = 36
        Ylen = 36
        rows = [[" "]*Xlen for i in range(0,Ylen)]
        rows[self.y][self.x] = '@'
        for angle in self.visible:
            for asteroid in self.visible[angle]:
                if asteroid.destruction_idx:
                    rows[asteroid.y][asteroid.x] = str(asteroid.destruction_idx)
                else:
                    rows[asteroid.y][asteroid.x] = '#'
        print("")
        for row in rows:
            print("".join(row))



asteroids = []

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '#':
            asteroids.append(Asteroid(x, y))


for counter, asteroid in enumerate(asteroids):
    for other_asteroid in asteroids:
        if other_asteroid is not asteroid:
            angle = asteroid.angle_to(other_asteroid)
            asteroid.add_visible(other_asteroid, angle)

max_visible_cnt = 0
best_asteroid = None
for cnt, asteroid in enumerate(asteroids):
    if len(asteroid.visible) > max_visible_cnt:
        max_visible_cnt = len(asteroid.visible)
        best_asteroid = asteroid
        print("best %d"%cnt)

print("Best asteroid for station is: x = %i, y = %i, cnt = %i"%(best_asteroid.x, best_asteroid.y, len(best_asteroid.visible)))


station =  best_asteroid
#station = asteroids[350] # from 1 part solution
for other_asteroid in asteroids:
    if other_asteroid is not station:
        other_asteroid.count_distance(station)
        angle = station.angle_to(other_asteroid)
        station.add_visible(other_asteroid, angle)

for angle in station.visible:
    station.visible_sorted.append(angle)



station.visible_sorted.sort()
station.visible_sorted.reverse()

for angle in station.visible:
    asteroids_list = station.visible[angle]
    asteroids_list.sort()

cnt = 0    
while cnt < 200:
    for angle in station.visible_sorted:
        asteroids_list = station.visible[angle]
        for asteroid in asteroids_list:
            if asteroid.destruction_idx == None:
                cnt += 1
                asteroid.destruction_idx = cnt
                station.draw_map()
                if cnt == 200:
                    print("200th asteroid:")
                    print(str(asteroid))
                    exit()
                break



print("fdsfds")