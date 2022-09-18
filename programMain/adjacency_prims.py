import networkx as nx
import matplotlib.pyplot as plt

global pathDistance

class place:
    def __init__(self,*args):
        if (len(args)==0):
            self.name=None
            self.connection=[]

        else:
            self.name=args[0]
            self.connection=[]
            #Structure of connection-> [["str(placeName)",int(Distance)]]

    def getName(self):
        return self.name

    def printConnection(self):
        print(self.connection)

#end of Class PLace


def addConnection(Placelist,adjmatrixList):
    count=0
    for i in (adjmatrixList):
        j=0
        while(j<len(i)):
            if(int(i[j])!=0):
                inserter=[]
                inserter.append(Placelist[j].name)
                inserter.append(int(i[j]))
                Placelist[count].connection.append(inserter)
            j+=1

        count+=1

                            #MERGE SOrt
def mergeSort(arr):
	if len(arr) > 1:

		mid = len(arr)//2

		L = arr[:mid]

		R = arr[mid:]

		mergeSort(L)

		mergeSort(R)

		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i][1] < R[j][1]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
	return arr

                                #TRAVERSE
def traverse(root,goal,path,Placelist):
    global pathDistance

    if(root.name==goal):
        return 0
    # end if 
    sortedConnection=mergeSort(root.connection)
    print(sortedConnection)
    # Selecting the minimum distant connection and connection which is not in the path 
    ZeroCount=0
    for sortElement in sortedConnection:
        indicator=1
        sortLength=len(sortedConnection)
        min=sortElement #Selecting a minimum 
        for pathObj in path:#Used to check whether the minimum is already in the path list
            if(pathObj.name==min[0]):
                indicator=0
                break
        if(indicator!=0):
            break
        else:# To check each connection is in the path or not
            ZeroCount=ZeroCount+1
        
        if(ZeroCount==sortLength):
            return -1
        
        # end for
    # end for
    for i in Placelist:
        if(min[0]==i.name):
            
            pathDistance=pathDistance+min[1]
            path.append(i)
            for i in path:
                print(i.name,end=" ")
            print()
            result=traverse(i,goal,path,Placelist)
            return result
        # end if
    # end for 
# end function
def PrimsAlgo(PlaceList,start,goal):
    global pathDistance
    path=[]
    pathDistance=0
    for i in PlaceList:
        if(i.name==start):
            startObj=i
            break
    path.append(startObj)
    result=traverse(startObj,goal,path,PlaceList)
    if(result==-1):
        for i in PlaceList:
            if(goal==i.name):
                print("!!! Destination not found using the Prim's algorithm due to its greed !!!")
                print("Final way till the DEADEND= ",end="")
    else:
        print("Destination found")
        print("path = ",end=" ")
    for each in path:
        print(each.name,end=" ")
        
    print()
    print("Path Distance = ",pathDistance)
    displayResult(path,PlaceList)
        
def displayInitial(PlaceList):
    processor=[]
    for node in PlaceList:
        for i in node.connection:
            # l is the list to be append into the list processor
            l=[]
            l.append(node.name)
            l.append(i[0])
            processor.append(l)
    G=nx.Graph()
    G.add_edges_from(processor)
    
    random_pos = nx.random_layout(G,seed=38) #This two lines to prevent the orientation change of the graph in result and initial state
    position=nx.spring_layout(G,pos=random_pos)
    nx.draw_networkx_nodes(G,position, node_size=200)
    nx.draw_networkx_edges(G,position, edgelist=G.edges(), edge_color='black')
    nx.draw_networkx_labels(G,position)
    plt.plot(1)
    plt.savefig('intialMap')
    plt.title("Complete Map")
    plt.axis('off')
    plt.figure()
    plt.show(block=False)
def displayResult(path,Placelist):
    # get a edge list for getting the path
    namePath=[]
    for each in path:
        namePath.append(each.name)

    getForm=[]
    count1=0
    count2=1
    while(count2<len(namePath)):
        inserter=[]
        inserter.append(namePath[count1])
        count1+=1
        inserter.append(namePath[count2])
        count2+=1
        getForm.append(inserter)
        
    processor=[]
    for node in Placelist:
        for i in node.connection:
            # l is the list to be append into the list processor
            l=[]
            l.append(node.name)
            l.append(i[0])
            processor.append(l)
            
    G=nx.Graph()
    G.add_edges_from(processor)
    random_pos = nx.random_layout(G, seed=38) #This two lines to prevent the orientation change of the graph in result and initial state #This two lines to prevent the orientation change of the graph in result and initial state
    position=nx.spring_layout(G,pos=random_pos)
    elist=[]
    for i in getForm:
        elist.append(i)
        nx.draw_networkx_nodes(G,position,node_size=450)
        nx.draw_networkx_edges(G,position, edgelist=G.edges(),edge_color='black')
        nx.draw_networkx_edges(G,position,edgelist=elist, width=7,edge_color='red')
        nx.draw_networkx_labels(G,position)
        plt.savefig('resultMap')
        plt.title("Minimum Spanning Tree")
        words="Path Distance = "+str(pathDistance)
        plt.axis('off')
        plt.text(0.93,1.2,words,transform=plt.gca().transAxes)
        plt.pause(1) # To constantly according to the current input which is here the path edge
    plt.show()
    
    
                                # MAIN PART
import csv
csvlist=[]
with open('n.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        csvlist.append(row)
    
allPlaces=[]
for i in range(len(csvlist)):
    print("Enter the name of place",i+1,": ")
    placeName=str(input())
    while(placeName=="" or placeName==" "):
        print("!!! Invalid entry !!!")
        print("Enter the name of place",i,": ")
        placeName=str(input())
    placeName=placeName.capitalize()
    allPlaces.append(place(placeName))


addConnection(allPlaces,csvlist)
print("hai")

displayInitial(allPlaces)
    
startChecker=1
start=str(input("Enter the start position name : "))
start=start.capitalize()
while(startChecker==1):
    for i in allPlaces:
        if(i.name==start):
            startChecker=0
            break
    if(startChecker==1):
        print("!! Entered start is not in the Map !!")
        start=str(input("Enter the start position name : "))
        start=start.capitalize()

goalChecker=1
goal=str(input("Enter the final position name : "))
goal=goal.capitalize()
while(goalChecker==1):
    for i in allPlaces:
        if(i.name==goal):
            goalChecker=0
            break
    if(goalChecker==1):
        print("!! Entered goal is not in the Map !!")
        goal=str(input("Enter the start position name : "))
        goal=goal.capitalize()
        
PrimsAlgo(allPlaces,start,goal)