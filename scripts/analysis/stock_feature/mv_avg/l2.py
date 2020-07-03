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

def setFeature(df,loop_len,feature_days):
    loop_len = 10
    for i in range(0,loop_len):
        #print(i)
        end_index = i + feature_days
        a1 = df.iloc[i:end_index]
        a1_list = a1[feature_column_list].values.tolist() 
        a1_list_flat = list(itertools.chain(*a1_list))
        a1_list_flat = a1_list_flat +[df['stock_date'][end_index],df['stock_index'][end_index]]
        df_list.append(a1_list_flat)
        if i % 10000 == 0:
            print(i)
    df_feature = pd.DataFrame(df_list).dropna()
    return df_feature


file1 = "/home/davidyu/stock/data/tmp_data/stock_feature/601398.csv"
df1 = pd.read_csv(file1)
df2 = df1.sort_values(["stock_index","stock_date"])
loop_len = 10
feature_days = 14

df_mvavg = addMvAvg(df2)
df,feature_column_list = makeFeature(df_mvavg)
#print(df.head(10))
data_feature = setFeature(df,loop_len,feature_days)
print("finish make feature dataframe")
df_list = []
#loop_len = df.shape[0]-1
data_dir = os.path.join(tmp_data_dict.get('stock_feature'),"mv_avg")
save_file = "mv_avg_feature.csv"
df_feature.to_csv(os.path.join(data_dir,save_file),index=0)

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




