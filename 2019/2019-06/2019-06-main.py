import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict

def read_input():
    with open("input.txt") as f:
        return [(line[0:3], line[4:7]) for line in f]
    return



class GameWindow():
    figure = None
    def __init__(self):
        if not GameWindow.figure:
            GameWindow.figure = plt.figure()
            GameWindow.figure.show()
            # self.axes = axes.Axes(self.figure)
    def clear(self):
        GameWindow.figure.clear()
    
    def draw(self):
        plt.draw()

raw_map = read_input()
orbit_dict = defaultdict(list)
for center, sattelite in raw_map:
    orbit_dict[center].append(sattelite)

gw =GameWindow()
gw.clear()
graph = nx.DiGraph(orbit_dict)
lengths_to_nodes = nx.single_source_shortest_path_length(graph, "COM")
total_length = sum([lengths_to_nodes[key] for key in lengths_to_nodes])
print("Total number of orbits is %d"%total_length)
pos = nx.random_layout(graph)
nx.draw_networkx_nodes(graph, pos)
nx.draw_networkx_edges(graph, pos = pos)
gw.draw()

print("end")
input()