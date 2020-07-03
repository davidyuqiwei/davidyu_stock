from davidyu_cfg import *
"""
combine the fin_report_feature  & stock_change_rate 
for modelling
"""


def combineData(fin_report_feature_dir,fin_report_name,change_rate_dir,change_rate_name,save_name,save_dir):
	## set data dir
	#tmp_data_dir = tmp_data_dict.get("financial_report")
	#fin_report_data = "fin_report_feature.csv"
	#change_rate_file = "/home/davidyu/stock/data/test/stock_change_rate_20170101_20171231.csv"
	fin_report_file = os.path.join(fin_report_feature_dir,fin_report_name)
	change_rate_file = os.path.join(change_rate_dir,change_rate_name)
	fin_report_df = pd.read_csv(fin_report_file)
	change_rate_df = pd.read_csv(change_rate_file,sep="\t")
	change_rate_df.columns = [x.split(".")[1] for x in change_rate_df.columns.tolist()]
	## merge the two dataframe
	df_merge1 = pd.merge(fin_report_df,change_rate_df,on=("stock_index"))
	## clean the data
	df_merge2 = df_merge1[df_merge1['cnt']==244]
	col_in = fin_report_df.columns.tolist()[:-1] + ["change_rate"]
	df_merge3 = df_merge2[col_in]
	df_merge3 = df_merge3.replace(-9999,np.nan) ## 180
	#save_file = "financial_report_ml_test_data.csv"
	df_merge3.astype(float).round(3).to_csv(os.path.join(save_dir,save_name),index=0)

if __name__=='__main__':
    fin_report_feature_dir = tmp_data_dict.get("financial_report")
    fin_report_name = "fin_report_feature.csv"
    change_rate_dir = "/home/davidyu/stock/data/test/"
    change_rate_name = "stock_change_rate_20170101_20171231.csv"
    save_name = "financial_report_ml_test_data.csv"
    save_dir = tmp_data_dict.get("financial_report")
    combineData(fin_report_feature_dir,fin_report_name,change_rate_dir,change_rate_name,save_name,save_dir)
