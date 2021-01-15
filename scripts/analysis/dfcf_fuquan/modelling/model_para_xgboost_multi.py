para_xgboost = {'booster': 'gbtree',
      #'objective': 'binary:logistic',
      'objective': 'multi:softprob',
      'num_class': 3,
      #'eval_metric': 'auc',
      'eval_metric': 'mlogloss',
      'max_depth': 8,
      'lambda': 3,
      'subsample': 0.75,
      'colsample_bytree': 0.5,
      'min_child_weight': 3,
      'eta': 0.025,
      'seed': 2019,
      'nthread': 8,
      'silent': 1,
      'gamma': 0.15,
      'learning_rate': 0.03
}
xgboost_loop_num = 500
