import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

G.add_node(1) # add a node
G.add_nodes_from([2,3]) # add a list of nodes
G.add_edge(1,2)
e = (2,3)
G.add_edge(*e)
G.add_edges_from([(1,3)])


DG=nx.DiGraph(G)

#nx.draw(G)
#nx.draw_random(G)
nx.draw_circular(DG)
#nx.draw_spectral(G)

plt.savefig("test.png")
