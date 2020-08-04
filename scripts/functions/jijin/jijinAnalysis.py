from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist,tmp_data_dict

class jijinAnalysis:
    def __init__(self):
        self.text = ""
        self.DF = ""
        self.df_select = ""
        self.data_fullname = ""
    def loadData(self):
        """
        first combine all the data and load it
        """
        data_dir = tmp_data_dict.get("jijin")
        data_name = os.path.join(data_dir,"jijin.csv")
        self.data_fullname = data_name
        df1 = pd.read_csv(data_name,header=None)
        #df1.columns = [基金名称,基金代码,持仓数量,占流通股比例,持股市值,占净值比例,stock_date,stock_index]
        df1.columns = ['jijin_name','jijin_code','chican_vol','liutong_ratio',
                'chigu_money','jingzhi_ratio','stock_date','stock_index']
        df1 = df1[df1["jijin_name"]!="基金名称"]
        df1["chigu_money"] = df1['chigu_money'].astype(float)
        self.DF = df1
        return self
    def countJijin(self):
        """
        count how many jijin is in the stock index
        """
        a2 = self.DF.groupby('stock_index')['jijin_name'].count()   
        jijin_count_df = a2.reset_index().sort_values('jijin_name',ascending=False)
        return jijin_count_df
    def totalMoneyJijin(self,stock_date):
        df2 = self.DF
        df2 = df2[df2["stock_date"]==stock_date]
        df2['chigu_money'] = df2['chigu_money'].astype(float)
        df3 = df2.groupby('stock_index')['chigu_money'].sum().reset_index().sort_values('chigu_money',ascending=False)
        return df3
    def singleStock(self,stock_index):
        """
        list the jijin money in a single stock,order by stock_date -- year-month
        """
        df2 = self.DF
        df3 = df2[df2["stock_index"]==stock_index]
        stock_jijin_count = df3.groupby("stock_date")["jijin_name"].count().reset_index().sort_values("stock_date")
        stock_chigu_money_sum = df3.groupby("stock_date")["chigu_money"].sum().reset_index().sort_values("stock_date")
        return stock_jijin_count,stock_chigu_money_sum
    def jijinOwnCount(self,stock_date):
        df1 = self.DF
        df2 = df1[df1["stock_date"]== stock_date]
        self.df_select = df2
        jijin_has_count = df2.groupby("jijin_name").count()["stock_index"].reset_index().sort_values("stock_index")
        
        return jijin_has_count


class jijinAna(jijinAnalysis):

    def test(self):
        return 1
    @staticmethod
    def jijinOwnStat(jijin_has_count,cnt_num,df_jijin_select):
        jijin_has_count2 = jijin_has_count[jijin_has_count["stock_index"]<=cnt_num]
        df_list = []
        for i in jijin_has_count2["jijin_name"].tolist():
            dd = df_jijin_select[df_jijin_select["jijin_name"]==i]
            df_list.append(dd)
        df_out = pd.concat(df_list)
        df_out = df_out[["jijin_name","stock_index","stock_date"]]
        return df_out
