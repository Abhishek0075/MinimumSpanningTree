import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_weighted_edges_from([ ['A','B',1],['A','C',2],[ 'C','B',10] ])

pos=nx.spring_layout(G)

nx.draw_networkx_nodes(G,pos, node_size=500)
nx.draw_networkx_edges(G,pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G,pos)
plt.show()