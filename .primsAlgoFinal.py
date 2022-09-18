from turtle import position
import networkx as nx
import matplotlib.pyplot as plt

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
        
    def addConnection(self,setConnect):
        i=0
        while(i<len(setConnect)):
            inserter=[]
            #The place name and distance are the connection details
            placeName=setConnect[i]
            i+=1
            placeName=placeName.capitalize()
            inserter.append(placeName)
            distance=int(setConnect[i])
            i+=1
            inserter.append(distance)
            self.connection.append(inserter)


    def printConnection(self):
        print(self.connection)
        
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

def traverse(root,goal,path,Placelist):
    
    if(root.name==goal):
        return 0
    # end if 
    sortedConnection=mergeSort(root.connection)
    print(sortedConnection)
    # Selecting the minimum distant connection and connection which is not in the path 
    ZeroCount=0
    for sortElement in sortedConnection:
        count=0
        length=len(path)
        sortLength=len(sortedConnection)
        min=sortElement
        for pathObj in path:
            if(pathObj.name==min[0]):
                count=1
                break
        if(count!=1):
            break
        else:
            ZeroCount=ZeroCount+1
        
        if(ZeroCount==sortLength):
            return -1
        
        # end for
    # end for
    for i in Placelist:
        if(min[0]==i.name):
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
    path=[]
    for i in allPlaces:
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

    nx.draw_networkx_nodes(G,position, node_size=500)
    nx.draw_networkx_edges(G,position, edgelist=G.edges(), edge_color='black')
    nx.draw_networkx_labels(G,position)
    plt.plot(1)
    plt.savefig('filename1')
    plt.title("Complete Map")
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
    
    nx.draw_networkx_nodes(G,position,node_size=500)
    nx.draw_networkx_edges(G,position, edgelist=G.edges(), edge_color='black')
    nx.draw_networkx_edges(G,position, edgelist=getForm, edge_color='red')
    nx.draw_networkx_labels(G,position)
    plt.title("Minimum Spanning Tree")
    plt.show()
    
    
                                # MAIN PART
import csv
csvlist=[]
with open('EnterTheMap.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        csvlist.append(row)


# nodeNo=len(csvlist)
allPlaces=[]
for i in csvlist:
    names=i[0]
    names=names.capitalize()
    placeObj=place(names)
    allPlaces.append(placeObj)
    

mover=0
for node in allPlaces:
    node.addConnection(csvlist[mover][2:])
    mover+=1
    
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
