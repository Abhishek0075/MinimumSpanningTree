class place:
    def __init__(self,*args):
        if (len(args)==0):
            self.attendence=None
            self.name=None
            self.connection=[]

        else:
            self.attendence=None
            self.name=args[0]
            self.connection=[]
            #Structure of connection-> [["str(placeName)",int(Distance)]]
    
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
            while((placeName=="") or (placeName==" ")):
                print("INVALID ENTRY")
                placeName=str(input("Enter the place name : "))
            inserter.append(placeName)
            print("Enter the distance between "+self.name+" and "+placeName+ " : ",end="")
            distance=int(input())
            inserter.append(distance)
            self.connection.append(inserter)

    def printConnection(self):
        print(self.connection)
        
def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i][1] < R[j][1]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
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
        return path
    # end if 
    sortedConnection=mergeSort(root.connection)
    print(sortedConnection)
    # Selecting the minimum distant connection and connection which is not in the path 

    for sortElement in sortedConnection:
        count=0
        length=len(path)
        min=sortElement
        for pathObj in path:
            if(pathObj.name==min[0]):
                count=1;
                break
        if(count!=1):
            break
        else:
            ZeroCount=ZeroCount+1
        
        if(ZeroCount==length):
            return path
        # end for
    # end for
    for i in Placelist:
        if(min[0]==i.name):
            
            path.append(i)
            for i in path:
                print(i.name,end="")
            print()
            traverse(i,goal,path,Placelist)
        # end if
    # end for 
# end function
def PrimsAlgo(PlaceList,goal):
    path=[]
    min=1000
    start=PlaceList[0]
    path.append(start)
    result=traverse(start,goal,path,PlaceList)
    
    for each in path:
        print(each.name,end="")

# main part

nodeNo=int(input("Enter the number of places in the map : "))
allPlaces=[]
# Creating the all node list
print("Enter the places In a way,the first entry is the start position")
for i in range(nodeNo):
    print("  Enter the name of place "+str(i+1)+" : ",end="")
    names=str(input())
    while((names=="") or (names==" ")):
                print("      !!! INVALID ENTRY !!!")
                print("  Enter the name of place "+str(i+1)+" : ",end="")
                names=str(input())
    placeObj=place(names)
    allPlaces.append(placeObj)
    
    
for node in allPlaces:
    connectionNo=int(input("Enter the number of places connected to "+node.getName()+" : "))
    node.addConnection(connectionNo)
# for node in allPlaces:
#     temp=node.getName()
#     print(temp)
#     node.printConnection()

PrimsAlgo(allPlaces,"Dasan")
