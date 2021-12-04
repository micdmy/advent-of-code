import logging

def read_input():
    with open("input.txt") as f:
        return [str(line) for line in f]
    return

class Position:
    def __init__(self):
        self.depth = 0
        self.horizontal = 0
    def move(self, order):
        if "down " in order:
            self.depth += int(order[5:])
        elif "up " in order:
            self.depth -= int(order[3:])
        elif "forward " in order:
            self.horizontal += int(order[8:])
        else:
            logging.error("bad order {}".format(order))
    def __str__(self):
        return ("Depth={} Horizontal={}".format(self.depth, self.horizontal))


class EnhancedPosition:
    def __init__(self):
        self.depth = 0
        self.horizontal = 0
        self.aim = 0
    def move(self, order):
        if "down " in order:
            self.aim += int(order[5:])
        elif "up " in order:
            self.aim -= int(order[3:])
        elif "forward " in order:
            x = int(order[8:])
            self.horizontal += x
            self.depth += self.aim * x
        else:
            logging.error("bad order {}".format(order))
    def __str__(self):
        return ("Depth={} Horizontal={} Aim={}".format(self.depth, self.horizontal, self.aim))
position = Position()
enhancedPosition = EnhancedPosition()
for order in read_input():
    position.move(order)
    enhancedPosition.move(order)
print("First part solution: " + str(position) + "multiplied=" + str(position.depth * position.horizontal))
print("Second part solution: " + str(enhancedPosition) + "multiplied=" + str(enhancedPosition.depth * enhancedPosition.horizontal))