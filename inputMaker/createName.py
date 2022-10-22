# Change the number of nodes in the loop range and get the output automatically in the verthe.txt file
import sys
f=open(r"C:\Users\abhir\OneDrive\Documents\GitHub\project_ds\csvFileAndNames\names.txt",'w')
sys.stdout=f
for i in range(20):
    if(i==19):
        print(i,end="")
        break
    print(i)
f.close()