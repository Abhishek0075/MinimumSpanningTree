
from turtle import distance


class place:
    def __init__(self,*args):
        if (len(args)==0):
            self.name=None
            self.connection=[]
        
        else:
            self.name=args[0]
            self.connection=[]

    def input_name(self):
        in=str(input("Enter the place name : "))
        self.name=in
class tree:
    def __init__(self,name) :
        a=place(name)
        self.start=a

    def add_connection(self,count):
        inserter=[]
        for i in range(count):
            placeName=str(input("Enter the place name : "))
            obj=place(placeName)
            inserter.append(obj)
            distance=int(input("Enter the distance from the root : "))
            inserter.append(distance)
            self.connection.append(inserter)
            
    
