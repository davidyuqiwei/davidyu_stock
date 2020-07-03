from davidyu_cfg import *
from functions.logModule.log_set import *
from functions.data_dir import *
class loadBasicInfo:
    def __init__(self):
        self.basic_info_df = self.basicInfoDF()
    def basicInfoDF(self):
        basic_info_dir = data_dict.get("basic_info")
        basic_info_df = pd.read_csv(os.path.join(basic_info_dir,"stock_basic_info.csv"))
        basic_info_df['stock_index'] = basic_info_df['code']
        basic_info_df['stock_index'] = [str(x).zfill(6) for x in basic_info_df['stock_index'].tolist()]
        logging.info("load basic info dataframe")
        return basic_info_df
    def combine_with_stock_basic_info(self,df_input):
        df_input['stock_index'] = [str(x).zfill(6) for x in df_input['stock_index'].tolist()]
        df1 = pd.merge(df_input,self.basic_info_df,how='left',on = ["stock_index"])
        return df1
if __name__ == "__main__":
    df1 = loadBasicInfo().basic_in_df
    print(df1.head(10))
