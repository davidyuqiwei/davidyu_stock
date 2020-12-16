import pandas as pd
from davidyu_cfg import *
from functions.rolling_regression import *
from functions.day_history.rollReg import rollRegDayHis
from functions.models.davidCluster import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist,tmp_data_dict

save_dir = tmp_data_dict.get("SH_index")
df3 = pd.read_csv(os.path.join(save_dir,"model_data.csv"))
feature_list = np.load("all_feature.npy").tolist()

Y = df3.slopes.values
X = df3[feature_list].values
#Y = np.array([0 if x <0 else 1 for x in Y])
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
