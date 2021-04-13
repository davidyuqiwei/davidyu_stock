from davidyu_cfg import *
from functions.common.parseToDF import *
from functions.get_datetime import *
from functions.common.dfProcess import dfProcess
from functions.data_dir import create_dir_if_not_exist

#file_in="longhubang_2021-03-14.txt"
file_in = sys.argv[1]
df1 = json_to_df(file_in,"GBK")
df2 = df1.get("data_out")

col_dict= {"SCode":"000591","SName":"太阳能","ClosePrice":"7.4","Chgradio":"9.9554","Dchratio":"17.128",
"JmMoney":"132786413.65","Turnover":"2508328205","Ntransac":"348921128","Ctypedes":"日涨幅偏离值达到7%的前5只证券",
"Oldid":"3961079","Smoney":"165155048.71","Bmoney":"297941462.36","ZeMoney":"463096511.07","Tdate":"2021-03-12",
"JmRate":"5.29","ZeRate":"18.46","Ltsz":"15074532074.6","Rchange1dc":"","Rchange1do":"","Rchange2dc":"","Rchange2do":"",
"Rchange3dc":"","Rchange3do":"","Rchange5dc":"","Rchange5do":"","Rchange10dc":"","Rchange10do":"","Rchange15dc":"",
"Rchange15do":"","Rchange20dc":"","Rchange20do":"","Rchange30dc":"","Rchange30do":"","Rchange1m":"26.27986347",
"Rchange3m":"62.99559472","Rchange6m":"64.44444445","Rchange1y":"99.48088439","SumCount":"","JGBSumCount":"",
"JGSSumCount":"","JGBMoney":"","JGSMoney":"","JGJMMoney":"","JD":"上海资金买入，成功率45.72%","DP":"上海资金买入，成功率45.72%"}
df2.columns = [x for x in col_dict.keys()]
#print(df2)
file_out=file_in.replace("txt","csv")
df2.to_csv(file_out,index=0)



