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
            distance=int(input("Enter the distance from the root : "))
            inserter.append(distance)
            self.connection.append(inserter)

    def printConnection(self):
        print(self.connection)
        

class tree:
    def __init__(self,name) :
        a=place(name)
        self.start=a

    
# main part
nodeNo=int(input("Enter the number of places in the map : "))
allPlaces=[]
# Creating the all node list
for i in range(nodeNo):
    print("Enter the name of place "+str(i+1)+" : ",end="")
    names=str(input())
    placeObj=place(names)
    allPlaces.append(placeObj)
    
for node in allPlaces:
    connectionNo=int(input("Enter the number of places connected to "+node.getName()+" : "))
    node.addConnection(connectionNo)

for node in allPlaces:
    node.printConnection()
