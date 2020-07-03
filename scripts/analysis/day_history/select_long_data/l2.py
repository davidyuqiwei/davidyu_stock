import pandas as pd
from davidyu_cfg import *
from functions.LinearReg import LinearReg
from functions.rolling_regression import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import itertools


def addMvAvg(df4):
    mv_days = [5,10,20,30]
    for i in mv_days:
        cols = 'mv'+str(i)
        df4[cols] = df4.groupby('stock_index')['adj_close'].rolling(i, min_periods=i).mean().reset_index()['adj_close']
    return df4

def featureProcess(df,col):
    df[col][df[col]>=0] = 1
    df[col][df[col]<0] = -1
    return df


def makeFeature(df,fea_cols=None):
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

#file1 = "/home/davidyu/stock/data/test/long_data_mv_avg.csv"
file1 = "/home/davidyu/stock/data/tmp_data/stock_feature/601398.csv"
df1 = pd.read_csv(file1)

df2 = df1.sort_values(["stock_index","stock_date"])
sort_col = "stock_date"
#df_slope = df2.groupby('stock_index').apply(rolling_regression, \
#        window=5,sort_col=sort_col,reg_col="adj_close")
print("finish rolling mean")
df_slope.index = [x for x in range(0,df_slope.shape[0])]
df_slope1 = df_slope[['stock_date','stock_index','adj_close','slopes','slope_num_in']]
#df3.groupby('stock_index')['adj_close'].apply(pd.rolling_apply, 3, lambda x: np.mean([i for i in x if i is not np.nan and i!='NaN']))
df_slope1 = addMvAvg(df_slope1)
df = df_slope1
df,feature_column_list = makeFeature(df)

print(df.head(10))
df_empty = pd.DataFrame()
feature_days = 14
#start_index = 50
for i in range(0,df.shape[0]-1):
    #print(i)
    end_index = i + feature_days
    a1 = df.iloc[i:end_index]
    slope = df['slopes'][end_index]
    if slope >=0:
        slope = 1
    else:
        slope = -1
    slope_num = df['slope_num_in'][end_index]
    a1_features = a1[feature_column_list]
    #feature_size = feature_days*len(feature_column_list)
    a1_list = a1[feature_column_list].values.tolist() 
    a1_list_flat = list(itertools.chain(*a1_list))
    df_X = pd.DataFrame(a1_list_flat).T
    df_X['slope'] = slope
    df_X['slope_num'] = slope_num
    df_empty = df_empty.append(df_X)
print("finish make feature dataframe")

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
pcamodel = PCA(n_components=30)
pca_data = pcamodel.fit_transform(X_train)
pca_test = pcamodel.fit_transform(X_test)

clf = GaussianNB().fit(X_train, y_train)
clf.score(X_test,y_test)
clf = GaussianNB().fit(pca_data, y_train)
clf.score(pca_test,y_test)

'''




