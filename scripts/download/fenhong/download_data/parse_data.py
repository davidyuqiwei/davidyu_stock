from davidyu_cfg import *
from functions.common.parseToDF import *
from functions.get_datetime import *
from functions.common.dfProcess import dfProcess
from functions.data_dir import create_dir_if_not_exist


data_dir = data_dict.get("fenhong")

raw_data_dir = os.path.join(data_dir,"raw_data")
save_data_dir = os.path.join(data_dir,"parse_data")
files = os.listdir(raw_data_dir)
#files = "2020-12-31_fenhong.txt"



cols={"MarketType":"深主板","Code":"000401","Name":"冀东水泥","SZZBL":0.0,"SGBL":"-","ZGBL":"-","XJFH":5.0,"GXL":0.0327011118378025,"YAGGR":"2021-03-17T00:00:00","YAGGRHSRZF":"-","GQDJRQSRZF":"-","GQDJR":"-","CQCXR":"-","CQCXRHSSRZF":"-","YCQTS":-2914193.0,"TotalEquity":1347522914.0,"EarningsPerShare":1.964,"NetAssetsPerShare":10.58616871,"MGGJJ":2.410443,"MGWFPLY":6.445077,"JLYTBZZ":5.533,"ReportingPeriod":"2020-12-31T00:00:00","ResultsbyDate":"2021-03-17T00:00:00","ProjectProgress":"董事会决议通过","AllocationPlan":"10派5.00元(含税)","RowNum":32476,"EITIME":"2021-03-16T17:55:18","EUTIME":"2021-03-16T17:55:18","NOTICEDATE":"2021-03-17T00:00:00","Iskcb":""}
col_names = [x for x in cols.keys()]

def parse_the_data(f1):
    file_in = os.path.join(raw_data_dir,f1)
    df1 = json_to_df(file_in)
    df2 = df1.get("data_out")
    df2.columns = col_names
    df2=df2.replace("[{MarketType","A")
    save_file = f1.replace("txt","csv")
    save_out_file = os.path.join(save_data_dir,save_file)
    df2.to_csv(save_out_file,index=0)
#parse_the_data(files)
for f1 in files:
    parse_the_data(f1)
