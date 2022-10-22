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
            while(m==n):
                n=rd.randint(0,self.dimension-1)
                m=rd.randint(0,self.dimension-1)
            randomNum=rd.randint(0,9)
            self.arr[m,n]=randomNum
            self.arr[n,m]=randomNum
            

import sys
f=open(r"C:\Users\abhir\OneDrive\Documents\GitHub\project_ds\csvFile\adj.csv","w")
sys.stdout=f
t=matrix(50)
t.createArr(100)
t.printArr()
f.close()