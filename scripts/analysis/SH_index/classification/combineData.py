import pandas as pd
from davidyu_cfg import *
from functions.rolling_regression import *
from functions.day_history.rollReg import rollRegDayHis
from functions.models.davidCluster import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist,tmp_data_dict

#data_file = "/home/davidyu/stock/data/SH_SZ_index/SH_index.csv"

save_dir = tmp_data_dict.get("SH_index")

rollreg = pd.read_csv(os.path.join(save_dir,"sh_index_rollReg.csv"))
kdj = pd.read_csv(os.path.join(save_dir,"sh_index_kdj.csv"))

feature_list = np.load("all_feature.npy").tolist()

def histCol(kdj,col_list):
    bin_labels_5 = [1,2,3,4,5]
    for i in col_list:
        kdj[i] = pd.qcut(kdj[i],q=[0,0.2,.4,.6,.8,1],
            labels=bin_labels_5)
    return kdj

df2 = pd.merge(rollreg,kdj)
df2 = df2[df2["slope_num_in"]==5]
df3 = df2[feature_list+['slopes']]
#print(df3.head(2))
slope_in = df3.slopes.values
df3["slopes"] = np.array([0 if x <0 else 1 for x in slope_in])
df3.round(2).to_csv(os.path.join(save_dir,"model_data.csv"),index=0)
'''
Y = df3.slopes.values
X = df3[feature_list].values
Y = np.array([0 if x <0 else 1 for x in Y])
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.3)
cl = davidCluster(x_train, y_train,x_test,y_test)
#cl.RandomForestClassifier()
#cl.printModelResult()
params={'booster':'gbtree',
        'objective': 'binary:logistic',
        'eval_metric': 'auc',
        'max_depth':5,
        'lambda':1,
        'subsample':0.6,
        'colsample_bytree':0.9,
        'min_child_weight':2,
        'n_estimators': 5000,
        'eta': 0.025,
        'seed':1400,
        'nthread':8,
        'max_delta_step': 0.2,
        'silent':1,
        'gamma':0.15,
        'learning_rate' : 0.01,
        'silent':False}

#cl.xgbGridClssifer(params)
cl.xgBoost(params)
cl.printModelResult()

'''
