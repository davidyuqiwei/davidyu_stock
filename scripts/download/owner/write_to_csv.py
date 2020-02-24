import csv
def write_to_csv(myfile,data):
    with open(myfile, 'wb') as f:
        wr = csv.writer(f, lineterminator='\n')
        for a1 in data:
            wr.writerow(a1)
