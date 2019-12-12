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
graph = nx.Graph(orbit_dict)
lengths_to_nodes = nx.single_source_shortest_path_length(graph, "COM")
total_length = sum([lengths_to_nodes[key] for key in lengths_to_nodes])
print("Total number of orbits is %d"%total_length)

def find_in_dict(searched_val, dictionary):
    for key, val in dictionary.items():
        if searched_val in val:
            return key 
    return None

#  part2:
YOU_orbits = find_in_dict("YOU", orbit_dict)
SAN_orbits = find_in_dict("SAN", orbit_dict)

dist_to_santa = nx.dijkstra_path_length(graph, YOU_orbits, SAN_orbits)
print("Number of orbits to santa is %d"%dist_to_santa)

pos = nx.random_layout(graph)
nx.draw_networkx_nodes(graph, pos)
nx.draw_networkx_edges(graph, pos = pos)
gw.draw()

print("end")
input()