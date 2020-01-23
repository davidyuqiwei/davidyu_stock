import pickle
from sklearn.externals import joblib
import random
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn import metrics

pkl_file = open('train_data.pkl', 'rb')
data_train = pickle.load(pkl_file)

pkl_file_test = open("test_data.pkl",'rb')
data_test = pickle.load(pkl_file_test)


x_train = data_train['x_train']
y_train = data_train['y_train']

x_test = data_test['x_test']
y_test = data_test['y_test']


'''
clf2 = RandomForestClassifier(n_estimators=20, max_depth=None,min_samples_split=2, random_state=0)
clf2.fit(x_train, y_train)
scores2 = cross_val_score(clf2, x_train, y_train)
print(scores2.mean())
'''


import xgboost as xgb
dtrain = xgb.DMatrix(x_train,label=y_train)
dtest = xgb.DMatrix(x_test)



#booster:
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
        'learning_rate' : 0.05}

watchlist = [(dtrain,'train')]
bst = xgb.train(params,dtrain,num_boost_round=100,evals=watchlist)

ypred = bst.predict(dtest)
y_pred = (ypred >= 0.5)*1

print ('AUC: %.4f' % metrics.roc_auc_score(y_test,y_pred))
print ('ACC: %.4f' % metrics.accuracy_score(y_test,y_pred))



