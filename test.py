class place:
    def __init__(self,*args):
        if (len(args)==0):
            self.name=None
            self.connection=[]

        else:
            self.name=args[0]
            self.connection=[]
            #Structure of connection-> [["placeName",Distance]]

    def inputName(self):
        inName=str(input("Enter the place name : "))
        self.name=inName

    def getName(self):
        return self.name
        
    def addConnection(self,count):
        for i in range(count):
            inserter=[]
            #The place name and distance are the connection details
            placeName=str(input("Enter the place name : "))
            inserter.append(placeName)
            print("Enter the distance between "+self.name+" and "+placeName+ " : ",end="")
            distance=int(input())
            inserter.append(distance)
            self.connection.append(inserter)

    def printConnection(self):
        print(self.connection)
        

def traverse(root,goal,path,Placelist):
    min=1000
    print("hai")
    print(path)
    if(root.name==goal):
        return path
    for x in root.connection:
        if(x[1]<min):
            min=x[1]
            minConnect=x[0]

    for i in Placelist:
        if(minConnect==i.name):
            for checker in path:
            path.append(i.name)
            print(path)
            traverse(i,goal,path,Placelist)
    
def PrimsAlgo(PlaceList,goal):
    path=[]
    min=1000
    start=PlaceList[0]
    path.append(start.name)
    traverse(start,goal,path,PlaceList)
    for i in path:
        print(i,end="")
    #obj->connection(list(list))->(list)
    # for x in start.connection:
    #     if(x[1]<min):
    #         min=x[1]
    #         minConnect=x[0]
    # for i in PlaceList:
    #     if(minConnect==i.name):
    #         for x in i.connection:
    #             k=[]

    # class graph:
    #     def __init__(self,nodes):
    #         self.places=nodes
                
    

# main part
nodeNo=int(input("Enter the number of places in the map : "))
allPlaces=[]
# Creating the all node list
print("Enter the places In a way,the first entry is the start position and final entry is the destination")
for i in range(nodeNo):
    print("  Enter the name of place "+str(i+1)+" : ",end="")
    names=str(input())
    placeObj=place(names)
    allPlaces.append(placeObj)
    
    
for node in allPlaces:
    connectionNo=int(input("Enter the number of places connected to "+node.getName()+" : "))
    node.addConnection(connectionNo)

for node in allPlaces:
    node.printConnection()

PrimsAlgo(allPlaces,"D")
