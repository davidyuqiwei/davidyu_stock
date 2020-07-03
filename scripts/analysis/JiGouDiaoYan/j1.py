from davidyu_cfg import *
from functions.connect_url import url_opener
from functions.ForDownload import generate_stock_index,stk_index_list_gen
from functions.data_dir import *
import time
from functions.make_dir import *
from functions.get_datetime import *  ## now_date,now_date_time = get_the_datetime()
from functions.LinearReg import LinearReg #
from functions.colNames import setColname
from functions.JiGouDiaoYan import jgdy
from functions.data_dir import *
from functions.config import GET_DAY_HISTORY_DATA_PATH,TMP_DATA_PATH



def loadData():
    data_dir = data_dict.get("JiGouDiaoYan")
    tmp_data_dir = tmp_data_dict.get("JiGouDiaoYan")
    cols = setColname().jigoudiaoyan()
    df = pd.read_csv(os.path.join(tmp_data_dir,"all_JiGouDiaoYan.csv"), \
            error_bad_lines=False,header=None)
    df.columns = cols
    return df

def getDiaoYanDF(start_date,end_date):
    df = loadData()
    df['stock_index'] = df['SCode'].apply(jgdy.jgdy.stockIndexCheck)
    df1 = df[df['stock_index'] != '-999999']
    df_diaoyan = df1[(df1['StartDate']>=start_date)&(df1['StartDate']<=end_date)].groupby('stock_index').count()['date'].reset_index().sort_values('date',ascending=False)
    return df_diaoyan

def headDiaoYanStockList(head_n,start_date,end_date):
    ''' 
    head_n : head n diaoyan number of the stock
    start_date: start_date = "2019-08-01"
    end_date: end_date = "2019-12-15"
    '''
    df_diaoyan = getDiaoYanDF(start_date,end_date)
    df_diaoyan_head_n = df_diaoyan.head(head_n)
    stk_diaoyan_list = df_diaoyan_head_n['stock_index'].tolist()
    stk_diaoyan_tup = tuple(stk_diaoyan_list)
    return stk_diaoyan_tup,df_diaoyan_head_n


if __name__ == "__main__":
    from functions.LinearReg import LinearReg
    from functions.day_history import kLines
    from functions.day_history.getDataFromSpark import *
    head_n = 100
    dy_start_date = '2020-06-20'
    stat_days = 10
    pred_days = 40
    stat_end_date,pred_start_date,pred_end_date = kLines.klineDate(dy_start_date,stat_days,pred_days).make_date()
    stat_dates_list = '_'.join([dy_start_date,stat_end_date,pred_start_date,pred_end_date])
    stk_diaoyan_tup,df_diaoyan_head_n = headDiaoYanStockList(head_n,dy_start_date,stat_end_date)
    print(df_diaoyan_head_n.head(10))
    '''
    para = {
            'stock_tuple': stk_diaoyan_tup,
            'start_date': pred_start_date,
            'end_date': pred_end_date
            }
    getSparkData = getDataFromSpark(para)
    getSparkData.getDataFromSpark()

    '''
    
    
    
    '''
        para = {
        'save_file_name':'spark_select_data.csv'
        }
    '''
    '''
    df1['stock_index'] = df1['stock_index'].apply(jgdy.jgdy.stockIndexCheck)
    df_slope = df1.groupby('stock_index').apply(lambda x: LinearReg.single_linear_reg(x,'adj_close')[0]).reset_index()
    df_slope.columns = ['code','slope']
    df_slope['stock_index'] = df_slope['code'].apply(jgdy.jgdy.stockIndexCheck)
    df_diaoyan_slope = pd.merge(df_slope,df1)
    df_diaoyan_slope = df_diaoyan_slope[["stock_index","slope"]].drop_duplicates()
    df_diaoyan_slope = df_diaoyan_slope.merge(df_diaoyan_head_n).sort_values('date',ascending=False) 
    tmp_data_dir = tmp_data_dict.get("JiGouDiaoYan")
    df_diaoyan_slope.to_csv(os.path.join(tmp_data_dir,"jgdy_slope"+stat_dates_list+".csv"),index=0)

    '''


    '''
    for i in range(0,head_n):
        stockIndex = stk_diaoyan_list[i]
        ## spark-submit input para
        slope = np.load(os.path.join(LINEAR_REG_PATH,"slope_out.npy")).tolist()
        slopes.append(slope)

    df_diaoyan_slope_100['slope'] = slopes
    print(df_diaoyan_slope_100.head(20))

    '''
#print(slope)
#df.groupby('stock_index')




