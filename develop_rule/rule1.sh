## download data
1. download data
  def download_data(stock_index,time_period,save_dir,if_need_transforn):
     ## time period : '2018-12-01'  '2018-12-03'
                # //  2017
                # // 2017 -3
     # ---- need transform return df for transform 

     #if need transform data
  pandas df
2. transform data
  def transform (df):
    return trans_df
  pandas df
3. save data
    def save_data(df,file_name):
      ## file_name  ::   save_dir+file_name
#--------------------------------#
#------???  check data ??? ------#
#--------------------------------#
4. store to hive 

for i in stock_list:
  download_data
  transform_data
  save_data
  store_to_hive
