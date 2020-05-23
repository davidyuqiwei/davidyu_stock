import pandas as pd
import os
from davidyu_cfg import *
import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

if __name__ == "__main__":
    file_name = os.path.join(tmp_data_path,"stock_feature","stock_feature1.csv")
    df_out = pd.read_csv(file_name)
    df_out1 = df_out.tail(4000)
    feature_start_index = 3
    feature_end_index = df_out.shape[1] -3

    df_feature = df_out1.iloc[:,feature_start_index:feature_end_index].values
    df_y_columns = df_out1.columns[feature_end_index:df_out.shape[1]]
    df_y = df_out1.close_change.values
    
    X_train, X_test, y_train, y_test  = train_test_split(df_feature,df_y, 
            test_size=0.1, random_state=42)


    #data = np.random.rand(5, 10)  # 5 entities, each contains 10 features
    #label = np.random.randint(2, size=5)  # binary target
    modelLR = LogisticRegression()
    modelLR.fit(X_train,y_train)
    modelLR.score(X_test,y_test)

    
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
    
    df_pred = pd.DataFrame(ypred)
    df_pred['y_test'] = y_test
    df_pred.columns = ['y_pred','ytest']
    df_pred[df_pred>0.5] = 1
    df_pred[df_pred<0.5] = 0
    df_pred['diff'] = df_pred['y_pred']-df_pred['ytest'] 
    pred_acc = df_pred[df_pred['diff'] == 0].shape[0]/df_pred.shape[0]
    print(pred_acc)



