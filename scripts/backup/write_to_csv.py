import csv
## list write to csv
def write_to_csv(myfile,data,colnames):
    with open(myfile, 'wb') as f:
        wr = csv.writer(f, lineterminator='\n')
        wr.writerow(colnames)
        for a1 in data:
            wr.writerow(a1)
