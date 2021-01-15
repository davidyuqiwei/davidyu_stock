from davidyu_cfg import *
from functions.common.loadModule.load_module_kdj import *
from functions.common.dfProcess import *


def makeFeature(df,fea_cols=None):
    '''
    feature mv_avg minus
    '''
    df = df.sort_values("dt")
    print("finish sort")
    feature_column_list = []
    if fea_cols is None:
        fea_cols = ['mv_avg5','mv_avg10','mv_avg20','mv_avg30']
    for i in fea_cols:
        for j in fea_cols:
            fea_name = '%s%s%s'%(i,'_',j)
            fea_name1 = '%s%s%s'%(j,'_',i)
            if i!=j and fea_name not in feature_column_list and fea_name1 not in feature_column_list:
                feature_column_list.append(fea_name)
                df[fea_name] = df[i]/df[j]
                #df = dfProcess.featureProcess(df,fea_name)
    return df,feature_column_list

def featureShift(DF,feature_list,max_shift=None):
    df1 = DF.copy(deep=True)
    df1 = df1.sort_values("dt")
    if max_shift is None:
        max_shift = 10
    feature_name_list = []
    for f1 in feature_list:
        for k in range(1,max_shift):
            new_name = f1+"_shift"+str(k)
            df1[new_name] = df1[f1].shift(k)
            feature_name_list.append(new_name)
    return df1,feature_name_list

def getAllDf(DF):
    rows = DF.shape[0]
    df_append = []
    for x in range(0,rows):
        x1 = DF.iloc[x,1][0]
        df_append.append(x1)
    df_all = pd.concat(df_append)
    return df_all

data_dir = data_dict.get("test")
#input_file = sys.argv[1]
input_file = "stock_index_mv_avg.csv"
df1 = pd.read_csv(os.path.join(data_dir,input_file))
df1 = cleanData.cleanColName(df1)
mv_feature = [ x for x in df1.columns.tolist() if "mv" in x ]
logging.info("make features")
a1 = df1.groupby("stock_index").apply(lambda x: makeFeature(x,mv_feature)).reset_index()
df_all = getAllDf(a1)
feature_column_list = a1.iloc[1,1][1]

logging.info("make features shift")
a3 = df_all.groupby("stock_index").apply(lambda x: featureShift(x,feature_column_list)).reset_index()
df_all = getAllDf(a3)
feature_column_list2 = a3.iloc[1,1][1]
## make all the features
feature_names_all = feature_column_list + feature_column_list2

logging.info("save data")
df_all.round(3).to_csv(os.path.join(data_dir,"stock_index_mv_avg_shift.csv"),index=0)
np.save(os.path.join(data_dir,"stock_index_mvavg_feature_name.npy"),feature_names_all)




