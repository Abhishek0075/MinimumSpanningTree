import sys # Important things
f = open("test.csv", 'w') # Important things
sys.stdout = f # Important things
i=0
while i<3:
    a=input("Write a number")
    h=str(2*a)
    print(h)
    print('Result%s'%h)
    i+=1
    
f.close() # Important things