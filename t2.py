    import networkx as nx
    random_pos = nx.random_layout(G, seed=38) #This two lines to prevent the orientation change of the graph in result and initial state #This two lines to prevent the orientation change of the graph in result and initial state
    position=nx.spring_layout(G,pos=random_pos)
    elist=[]
    colorlist=['green','red']
    for i in range(len(getForm-2)):
        if(i%2==0):
            colorlist.insert(1,"")
    for i in getForm:
        elist.append(i)
        nx.draw_networkx_nodes(G,position,node_size=450)
        nx.draw_networkx_edges(G,position, edgelist=G.edges(),edge_color='black')
        nx.draw_networkx_edges(G,position, edgelist=elist,width=7,edge_color='red')
        nx.draw_networkx_labels(G,position)
        plt.savefig('resultMap')
        plt.title("Minimum Spanning Tree")
        words="Path Distance = "+str(pathDistance)
        plt.text(0.93,0.73,words,transform=plt.gca().transAxes)
        plt.pause(1) # To constantly according to the current input which is here the path edge
    plt.show()