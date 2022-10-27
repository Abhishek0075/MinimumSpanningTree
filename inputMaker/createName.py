# Change the number of nodes in the loop range and get the output automatically in the verthe.txt file
import sys
numberOfNames=50
f=open(r"C:\Users\abhir\OneDrive\Documents\GitHub\project_ds\csvFileAndNames\names.txt",'w')
sys.stdout=f
for i in range(numberOfNames):
    if(i==(numberOfNames-1)):
        print(i,end="")
        break
    print(i)
f.close()