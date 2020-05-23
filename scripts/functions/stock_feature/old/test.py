import pandas as pd
import os
class ReadCsvData(object):
    def __init__(self):
        self.test = 1
    def read_csv_clean(self,data_dir,file_name):
        df1 = pd.read_csv(os.path.join(data_dir,file_name))
        df1 = df1.dropna().round(2)
        return df1
        #return df1

class clean_data(ReadCsvData):
    def __init__(self):
        self.DF = 'a'
        self.tt = 2
    def read_csv_clean(self,data_dir,file_name):
        self.DF = super(clean_data,self).read_csv_clean(data_dir,file_name)
        return self
    def clean_colname(self):
        name_forward_string = self.DF.columns[0].split(".")[0]+"."
        self.DF.columns = [x.replace(name_forward_string,"") for x in self.DF.columns.tolist()]
        df1 = self.DF
        return df1

if __name__ == '__main__':
    data_dir = "/home/davidyu/stock/data/test/for_lstm"
    file_name = "SH_index.csv"
    #aa = clean_data(data_dir,file_name)
    df1 = clean_data().read_csv_clean(data_dir,file_name).clean_colname()
    print(df1)
    #df1 = aa.read_csv_clean(data_dir,file_name).clean_colname()

