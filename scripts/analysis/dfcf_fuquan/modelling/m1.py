import pandas as pd
from davidyu_cfg import *
from functions.rolling_regression import *
from functions.stock_feature.mergeData import mergeData
import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler


data_file = "/home/davidyu/stock/data/test/dfcf_fuquan_kdj_reg.csv"
column_names = ["stock_index","dt","slope","slope_num_in","days_default","slope_cls","slope_cls2","rsi_6",
    			"rsi_12","rsi_24","kdjk","kdjd","kdjj","macdh","boll_ub","boll_lb","boll_ratio"]
feature_columns = ["rsi_6","rsi_12","rsi_24","kdjk","kdjd","kdjj","macdh","boll_ub","boll_lb","boll_ratio"]
y_column = "slope_cls"

def make_train_test_data(data_file,column_names,feature_columns,y_column,test_size=0.8,random_state=5):
    df1 = pd.read_csv(data_file,sep="\t",header=None)
    df1.columns = column_names
    df2 = df1[df1["slope_num_in"]==5]
    df_y = df2[y_column]
    feature_all = feature_columns
    df_feature = df2[feature_all]
    df_y[df_y==-1]=0
    X_train, X_test, y_train, y_test  = train_test_split(df_feature,df_y,
    			test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test
X_train, X_test, y_train, y_test = make_train_test_data(data_file,column_names,feature_columns,y_column,test_size=0.3,random_state=1)

ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test=ss.transform(X_test)


dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test)
params={'booster':'gbtree',
    		'objective': 'binary:logistic',
    		'eval_metric': 'auc',
    		'max_depth':7,
    		'lambda':15,
    		'subsample':0.75,
    		'colsample_bytree':0.75,
    		'min_child_weight':1,
    		'eta': 0.025,
    		'seed':0,
    		'nthread':8,
    		'silent':1,
    		'gamma':0.15,
    		'learning_rate' : 0.1}
watchlist = [(dtrain,'train')]
num_boost_round = 50
bst = xgb.train(params,dtrain,num_boost_round=num_boost_round,evals=watchlist)
feature_import = pd.DataFrame(bst.get_fscore(),index=[0]).T.reset_index()
feature_import.columns = ["feature_name","score"]
feature_import["feature_name"] = feature_columns
print("num_boost_round: "+str(num_boost_round ))
print("feature importance")
print(feature_import.sort_values("score",ascending=False))


def train_cut_score(bst,dtrain):
    b1 = bst.predict(dtrain)
    b1 = [np.round(x,3) for x in b1.tolist()]
    #b2 = pd.DataFrame([y_train.values.tolist(),b1]).T
    b2 = pd.DataFrame(y_train.values.tolist())
    b2["pred"] = b1
    b2.columns = ["slope_cls","pred"]
    d_bins = b2["pred"].quantile([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,0.96,0.98])
    groups = pd.cut(b2['pred'],bins=[0]+d_bins.values.tolist()+[1])
    b2["groups"] = groups
    b3 = b2.groupby("groups").sum()["slope_cls"].reset_index()
    b3["count"] = b2.groupby("groups").count()["slope_cls"].values.tolist()
    b3["pos_ratio"] = b3["slope_cls"]/b3["count"]
    print("group prediction score")
    print(b3)
    thres = b2["pred"].quantile(0.98)
    print("threshold: "+str(np.round(thres,3)))
    return thres

def test_score(bst,dtest,thres):
    ypred = bst.predict(dtest)
    df_pred = pd.DataFrame(y_test.tolist(),ypred.tolist()).reset_index()
    df_pred.columns = ["pred_test","obs_test"]
    #thres = df_pred["pred_test"].quantile(0.98)
    df_pred["pred_test"][df_pred["pred_test"]>thres]=1
    df_pred["pred_test"][df_pred["pred_test"]<=thres]=0
    pred_ratio = df_pred[df_pred["pred_test"]==df_pred["obs_test"]].shape[0]/df_pred.shape[0]
    pos_ratio = df_pred[df_pred["pred_test"]==1].sum()[1]/df_pred[df_pred["pred_test"]==1].sum()[0]
    print("pred postive ratio: "+str(np.round(pos_ratio,3)))

thres = train_cut_score(bst,dtrain)
test_score(bst,dtest,thres)


















'''



b2.groupby("groups").count()["slope_cls"]




model = XGBClassifier()
model.fit(X_train, y_train)

x1 = model.predict(X_train)


aa = pd.DataFrame([feature_all,model.feature_importances_]).T
aa.columns = ["feature","score"]
aa.sort_values("score",ascending=False).head(30)

'''





