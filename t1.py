import csv
csvlist=[]

with open('give.csv') as file_obj:
    reader_obj = csv.reader(file_obj)

    for row in reader_obj:
        csvlist.append(row)
    
print(csvlist)