import pandas as pd
from davidyu_cfg import *
from functions.LinearReg import LinearReg
from functions.rolling_regression import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import itertools


def addMvAvg(df4):
    '''
    add moving average of a data frame
    '''
    mv_days = [5,10,20,30]
    for i in mv_days:
        cols = 'mv'+str(i)
        df4[cols] = df4.groupby('stock_index')['adj_close'].rolling(i, min_periods=i).mean().reset_index()['adj_close']
    return df4

def featureProcess(df,col):
    '''
    >=0 =1
    <= =-1
    '''
    df[col][df[col]>=0] = 1
    df[col][df[col]<0] = -1
    return df


def makeFeature(df,fea_cols=None):
    '''
    feature mv_avg minus
    '''
    feature_column_list = []
    fea_cols = ['mv5','mv10','mv20','mv30']
    for i in fea_cols:
        for j in fea_cols:
            fea_name = '%s%s%s'%(i,'_',j)
            fea_name1 = '%s%s%s'%(j,'_',i)
            if i!=j and fea_name not in feature_column_list and fea_name1 not in feature_column_list:
                feature_column_list.append(fea_name)
                df[fea_name] = df[i]-df[j]
                df = featureProcess(df,fea_name)
    return df,feature_column_list

def setFeature(df,loop_len,feature_days,feature_column_list):
    '''
    选定一个矩阵内的特征
    feature_column_list: 特征列
    '''
    feature_d = [str(x) for x in range(1,feature_days+1)]
    feature_cols = [[y+'_'+x for y in feature_column_list] for x in feature_d]
    featureColName = list(itertools.chain(*feature_cols))
    df_list = []
    if loop_len == 'test':
        loop_len = 100
    else:
        loop_len = df.shape[0]
    for i in range(0,loop_len):
        #print(i)
        try:
            end_index = i + feature_days
            df_square = df.iloc[i:end_index]
            a1_list = df_square[feature_column_list].values.tolist() 
            a1_list_flat = list(itertools.chain(*a1_list))
            a1_list_flat = a1_list_flat +[df['stock_date'][end_index],df['stock_index'][end_index]]
            df_list.append(a1_list_flat)
        except:
            pass
        if i % 1000 == 0 and i>1:
            logging.info("loop {}".format(str(i)))
    col_names = featureColName+['stock_date','stock_index']
    df_feature = pd.DataFrame(df_list).dropna()
    df_feature.columns = col_names
    return df_feature
if __name__ == "__main__":
    file1 = "/home/davidyu/stock/data/tmp_data/stock_feature/601398.csv"
    df_raw = pd.read_csv(file1).sort_values(["stock_index","stock_date"])
    df1 = df_raw[['stock_date','stock_index','adj_close']]
    feature_days = 14
    loop_len = 'tes'
    df_mvavg = addMvAvg(df1)
    '''
    raw feature dataframe
    '''
    df,feature_column_list = makeFeature(df_mvavg)
    '''
    feature Names
    '''
    feature_d = [str(x) for x in range(1,feature_days+1)]
    feature_cols = [[y+'_'+x for y in feature_column_list] for x in feature_d]
    featureColName = list(itertools.chain(*feature_cols))
    """
    every stock index make feature matrix
    """
    df_feature = df.groupby('stock_index').apply(lambda x:setFeature(x,loop_len,feature_days,feature_column_list))
    df_feature1 = df_feature.reset_index(drop=True)
    df_feature_final = df_feature1[df_feature.columns.tolist()]
    #feature_size = len(feature_column_list)*feature_days
    #aa.iloc[]
    logging.info("finish make feature dataframe")
    data_dir = os.path.join(tmp_data_dict.get('stock_feature'),"mv_avg")
    save_file = "mv_avg_feature.csv"
    df_feature_final.to_csv(os.path.join(data_dir,save_file),index=0)



'''
df_model = df_empty.dropna()
feature_size = len(feature_column_list)*feature_days
df_feature = df_model.iloc[:,0:feature_size]
df_y = df_model.slope.values

X_train, X_test, y_train, y_test  = train_test_split(df_feature,df_y,
        test_size=0.1, random_state=42)

modelLR = LogisticRegression()
modelLR.fit(X_train,y_train)
print(modelLR.score(X_test,y_test))

from sklearn.naive_bayes import GaussianNB
from sklearn.decomposition import PCA

'''

'''
pcamodel = PCA(n_components=30)
pca_data = pcamodel.fit_transform(X_train)
pca_test = pcamodel.fit_transform(X_test)

clf = GaussianNB().fit(X_train, y_train)
clf.score(X_test,y_test)
clf = GaussianNB().fit(pca_data, y_train)
clf.score(pca_test,y_test)

'''




