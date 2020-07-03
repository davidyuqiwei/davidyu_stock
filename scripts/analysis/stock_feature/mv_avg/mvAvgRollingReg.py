import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import gc
import random
import numpy as np
def main():
    df_fea = pd.read_csv("/home/davidyu/stock/data/tmp_data/stock_feature/mv_avg/mv_avg_feature.csv")
    df_fea['stock_index'] = df_fea['stock_index'].astype(str)
    df1 = df_fea.sample(frac=0.5)
    del df_fea
    gc.collect()
    aa=df1['mv5_mv10_1'].astype(str).values.tolist() 
    print(df1.shape)
    print('add new feature')
    feature_columns = df1.columns.tolist()[:-2]
    feature_columns_raw = df1.columns.tolist()[:-2]
    new_feature_list = []
    new_feature_name = []
    for i in random.sample(feature_columns,20):
        for j in random.sample(feature_columns,20):
            new_col1 = i+'_'+j
            new_col2 = j+'_'+i
            if new_col1 not in feature_columns and new_col2 not in feature_columns:
                feature_columns_raw.append(new_col1)
                f1 = df1[i].astype(str).values.tolist()
                f2 = df1[j].astype(str).values.tolist()
                new_col_val = [str(f2[i])+'_'+str(x) for i,x in enumerate(f1)]
                new_feature_list.append(new_col_val)
                #df1[new_col1] = new_col_val
                del f1,f2
                gc.collect()   
    feature_columns = feature_columns_raw
    df1 = df1.replace('1.0_1.0',1)
    df1 = df1.replace('1.0_-1.0',2)
    df1 = df1.replace('-1.0_1.0',3)
    df1 = df1.replace('-1.0_-1.0',4)
    print(df1.shape)
    df2 = pd.read_csv("/home/davidyu/stock/data/tmp_data/stock_feature/rolling_regression/rolling_all.csv")
    df2['stock_index'] = df2['stock_index'].astype(str)
    
    df_merge = pd.merge(df2,df1,on=("stock_date","stock_index"))
    
    print('del df1 df2')
    del df1,df2
    gc.collect()
    df_merge1 = df_merge.dropna()
    df_merge1['slopes'] = df_merge1['slopes'].astype(float)
    def featureProcess(df,col):
        '''
        >=0 =1
        <= =-1
        '''
        df[col] = df[col].astype(float)
        df[col][df[col]>=0] = 1
        df[col][df[col]<0] = -1
        return df
    
    
    df_merge1 = df_merge1[df_merge1['slopes']!=0]
    df_merge1 = featureProcess(df_merge1,'slopes')
    
    df_feature = df_merge1[feature_columns].values
    df_y = df_merge1.slopes.values
    
    del df_merge1,df_merge
    gc.collect()
    X_train, X_test, y_train, y_test  = train_test_split(df_feature,df_y,
        test_size=0.1, random_state=42)
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import ExtraTreesClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import cross_val_score
    #clf1 = DecisionTreeClassifier(max_depth=None, min_samples_split=2,random_state=0)
    #scores1 = cross_val_score(clf1, X_train, y_train)
    #print(scores1.mean())
    
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    clf.fit(X_train, y_train)
    print(clf.score(X_test,y_test))
    
    aa = pd.DataFrame(clf.feature_importances_)
    aa['feature_name'] = feature_columns
    aa.columns = ['important_score','feature_name']
    aa2 = aa.sort_values('important_score')
    print(aa2)
    score = np.round(clf.score(X_test,y_test),2)
    return score,aa2.tail(2).values.tolist()

if __name__ == "__main__":
    score_list = []
    fea_import = []
    for i in range(0,2):
        score,i_list = main()
        score_list.append(score)
        fea_import.append(i_list)




'''
modelLR = LogisticRegression(C=1000)
modelLR.fit(X_train,y_train)
print(modelLR.score(X_test,y_test))
from sklearn.metrics import confusion_matrix
y_pred = modelLR.predict(X_test)
print(u"混淆矩阵",confusion_matrix(y_true=y_test,y_pred=y_pred))



from sklearn.naive_bayes import GaussianNB
from sklearn.decomposition import PCA

clf = GaussianNB().fit(X_train, y_train)
clf.score(X_test,y_test)

clf = GaussianNB().fit(pca_data, y_train)
clf.score(pca_test,y_test)

'''



'''
from sklearn import svm
clf=svm.SVC()
clf.fit(X_train, y_train)
print(clf.score(X_test,y_test))

'''


