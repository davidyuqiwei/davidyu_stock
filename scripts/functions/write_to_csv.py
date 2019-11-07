import csv
## list write to csv
def write_to_csv(myfile,data):
    with open(myfile, 'w') as f:
        #print(data)
        wr = csv.writer(f, lineterminator='\n')
        #wr = csv.writer(f, dialect = ("excel"))
        #wr.writerow(["date","open","high","close","low","volume","trade_amount","fuquan_factor"])
        for a1 in data:
            wr.writerow(a1)
