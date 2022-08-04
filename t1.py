# l=[]
# class test:
#     def __init__(self,name):
#         self.name=name
    
#     def create(self,num):
#         l.append(self)
#         for i in range (num):
#             n=str(input("Enter the name : "))
#             t=test(n)
#             l.append(t)
    
#     def out(self):
#         for i in (l):
#             print(i.name)

# temp=test("Abhishek")
# temp.create(3)
# temp.out()

# l=[]
# for i in range (3) :
#     t=[]
#     s=str(input("Enter a name : "))
#     t.append(s)

#     n=int(input("Enter a age : "))
#     t.append(n)
#     print("")
#     l.append(t)

# print((l[1])[0],(l[1])[1])

class place:
    def __init__(self,*args):
        if (len(args)==0):
            self.name="hai"
            self.connection=[]
        
        else:
            self.name=args[0]
            self.connection=[]
# Dasa ni mess ano
    def printname(self):
        print(self.name)

a=place()
# a.printname()

b=place("Dasan",1)
b.printname()



