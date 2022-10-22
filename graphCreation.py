
import networkx as nx
import matplotlib.pyplot as plt
processor=[["A","B"],["A" ,"C"],["B","C"],["B","D"],["B","E"],["E","A"]]
G=nx.Graph()
G.add_edges_from(processor)
pos=nx.spring_layout(G)

val_map={'A':1.00,'E':0.00}

value=[val_map.get(nodes,0.25) for nodes in G.nodes()]
print(value)
nx.draw_networkx_nodes(G,pos,cmap=plt.get_cmap('Greens') ,node_size=500,node_color=value)
nx.draw_networkx_edges(G,pos, edgelist=G.edges(), edge_color='red')
nx.draw_networkx_labels(G,pos)
plt.show()