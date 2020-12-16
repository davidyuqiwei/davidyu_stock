import pandas as pd
from davidyu_cfg import *
from functions.rolling_regression import *
from functions.stock_feature.mergeData import mergeData

data_dir = data_dict.get("test")

roll_reg = pd.read_csv(os.path.join(data_dir,"sh_index_rollreg_result.csv"))

feature_kdj = pd.read_csv(os.path.join(data_dir,"sh_index_kdj.csv"))
feature_mvAvg = pd.read_csv(os.path.join(data_dir,"sh_mv_avg.csv"))

a1 = pd.merge(roll_reg,feature_kdj,on=["dt","stock_index"], how='left')
a2 = pd.merge(a1,feature_mvAvg,on=["dt","stock_index"], how='left')
a2 = a2[a2["slope_num_in"]==5]
os.chdir(data_dir)
fea1 = np.load("kdj_feature_name.npy")
fea2 = np.load("sh_index_mvavg_feature_name.npy")

feature_all = fea1.tolist()+fea2.tolist()
feature_all = list(set(feature_all))


df1 = a2[["slopes"]+feature_all]
df2 = df1.dropna()



import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier


df_y = df2["slopes"]
df_y[df2["slopes"]>=0]=1
df_y[df2["slopes"]<0]=0
df_feature = df2[feature_all]

X_train, X_test, y_train, y_test  = train_test_split(df_feature,df_y,
    test_size=0.1, random_state=42)


'''
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test)
params={'booster':'gbtree',
            'objective': 'binary:logistic',
            'eval_metric': 'auc',
            'max_depth':4,
            'lambda':15,
            'subsample':0.75,
            'colsample_bytree':0.75,
            'min_child_weight':1,
            'eta': 0.025,
            'seed':0,
            'nthread':8,
            'silent':1,
            'gamma':0.15,
            'learning_rate' : 0.05}
watchlist = [(dtrain,'train')]
bst = xgb.train(params,dtrain,num_boost_round=100,evals=watchlist)
ypred = bst.predict(dtest)

'''


model = XGBClassifier()
model.fit(X_train, y_train)
model.predict(X_train)

df_train = pd.DataFrame(model.predict(X_train),y_train)
df_train = df_train.reset_index()

aa = pd.DataFrame([feature_all,model.feature_importances_]).T
aa.columns = ["feature","score"] 
aa.sort_values("score",ascending=False).head(30)

import_features = aa.sort_values("score",ascending=False).head(30)["feature"].values.tolist()
df_feature_import = df1[["slopes"]+import_features]
df_feature_import["slopes"][df_feature_import["slopes"]>=0] = 1
df_feature_import["slopes"][df_feature_import["slopes"]<0] = 0
#df_feature_import.to_csv("df_feature_import.csv",index=0)














