import pandas as pd
from davidyu_cfg import *
from functions.stockstats.stockStats import *
from functions.rolling_regression import *
from functions.stock_feature.mergeData import mergeData
from functions.models.davidCluster import davidCluster
from functions.logModule.log_set import *
# remove first two lines


#file_in = "/home/davidyu/stock/data/tmp_data/qianlong_day_history/test/000089.txt"
def loadCombineData(data_dir):
    frames = []
    files = os.listdir(data_dir)
    for f in files:
        try:
            file_in = os.path.join(data_dir,f)
            df1 = pd.read_csv(file_in,error_bad_lines=False,encoding="latin1",sep="\t",header=None)
            df2 = df1.iloc[:,0:7]
            df2.columns = ["stock_date","open","high","low","close","volume","money" ] 
            df2["stock_index"] = f[0:6]
            frames.append(df2)
        except:
            logging.info(f)
            pass        
    df_all = pd.concat(frames)
    return df_all 

def cleanData(df2,columns_list):
    # clean the noise str
    for col in columns_list:
        df2[col] = [x.replace("    ","") for x in df2[col].tolist()]
        df2 = df2.replace("----",np.nan)
    # columns data to float
    for i in columns_list:
        df2[i] = df2[i].astype(float)
    return df2

def makeModelData(data_dir,columns_list):
    data_all = loadCombineData(data_dir)
    df4 = cleanData(data_all,columns_list).dropna()
    df_roll_reg = df4.groupby("stock_index").apply(lambda x: rolling_regression(x,regression_window,"stock_date","close"))
    
    df2 = df_roll_reg.reset_index(drop=True) 
    df2 = df2[df2["slope_num_in"] ==5]
    #df2["slopes"] = mergeData.regPN(df2,'slopes')["slopes"]
    df_final= df2[columns_list + ["slopes"]]
    return df_final
if __name__ == "__main__":
    #qianlong_columns_list = ["kdj_j","kdj_k","kdj_d","macd_dif","macd","macd_dif_macd"]
    #feature_list = ['kdjk','kdjd','kdjj','macdh',"rsi_6","close"]
    
    regression_window = 5
    raw_data_dir = tmp_data_dict.get("qianlong_day_history")
    data_dir = os.path.join(raw_data_dir,"process")
    files = os.listdir(data_dir)
    df1 = loadCombineData(data_dir)
    #df_final = makeModelData(data_dir,qianlong_columns_list)
    df1["stock_date"] = df1["stock_date"].replace("/","-")
    stock = DF_to_StockDataFrame(df1)
    

    '''
    tmp_path = raw_data_dir
    
    #save_file = "test.csv"
    #save_file_name = os.path.join(tmp_data_path,save_file)
    #df3.to_csv(save_file_name,index=0)
    
    from sklearn.model_selection import GridSearchCV, train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import cross_val_score
    
    df_final["slopes"] = mergeData.regPN(df_final,'slopes')["slopes"]
    df_final["slopes"][df_final["slopes"]==-1]
    feature_list = ["kdj_k","kdj_d","kdj_j","macd_dif","macd","macd_dif_macd"]
    Y = df_final.slopes.values
    X = df_final[feature_list].values
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.3)
    
    cl1 = davidCluster(x_train, y_train,x_test,y_test)
    cl2 = cl1.RandomForestClassifier()
    cl2.printModelResult()
    print(cl2.model.feature_importances_)
    
    
    #cl2 = cl1.xgBoost()
    
    

    '''
