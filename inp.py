import numpy as np
import random as rd

class matrix:
    def __init__(self,num) -> None:
        self.dimension=num
        self.arr=np.zeros((num,num),dtype=int)
        
    def printArr(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if(j==self.dimension-1):
                    print(self.arr[i][j],end="")
                    break
                print(self.arr[i][j],end=",")
            print()
    def createArr(self,numElement):
        for i in range(numElement):
            n=rd.randint(0,self.dimension-1)
            m=rd.randint(0,self.dimension-1)
            randomNum=rd.randint(0,9)
            self.arr[m,n]=randomNum
            self.arr[n,m]=randomNum
            
        
t=matrix(50)
t.createArr(90)
t.printArr()

