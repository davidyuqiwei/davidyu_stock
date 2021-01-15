para_xgboost = {'booster': 'gbtree',
      'objective': 'binary:logistic',
      #'objective': 'multi:softmax',
      #'num_class': 6,
      'eval_metric': 'auc',
      #'eval_metric': 'mlogloss',
      'max_depth': 5,
      'lambda': 0.4,
      'subsample': 0.75,
      'colsample_bytree': 0.75,
      'min_child_weight': 1,
      'eta': 0.025,
      'seed': 0,
      'nthread': 8,
      'silent': 1,
      'gamma': 0.15,
      'learning_rate': 0.1
}
xgboost_loop_num = 1000
