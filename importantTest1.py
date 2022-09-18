import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_nodes_from([0,1,2])
G.add_weighted_edges_from([[0, 1, 3.0], [1, 2, 7.5]])
random_pos = nx.random_layout(G,seed=23) #This two lines to prevent the orientation change of the graph in result and initial state #This two lines to prevent the orientation change of the graph in result and initial state
position=nx.spring_layout(G,pos=random_pos)
nx.draw_networkx_nodes(G,position,node_size=450)
nx.draw_networkx_edges(G,position, edgelist=G.edges(),edge_color='black')
print(G.edges())
weight=nx.get_edge_attributes(G,'weight')
print(weight)
nx.draw_networkx_edge_labels(G,position,edge_labels=weight)
nx.draw_networkx_labels(G,position)
plt.show()