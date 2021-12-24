import csv

with open('./names/yob2020.txt') as file:
    csv_in = csv.reader(file)

    out_file = open('./posnames.csv', 'w+') 
    csv_out = csv.writer(out_file)

    for i in range(31271):
        row = csv_in.__next__()
        csv_out.writerow([row[0]])

    out_file.close()

    
