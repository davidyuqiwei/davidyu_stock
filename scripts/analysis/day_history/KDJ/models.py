import xgboost as xgb
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score


file_name = "/home/davidyu/stock/data/test/SH_index_kdj_macd_rsi_test.csv"
df1 = pd.read_csv(file_name)
df1["slopes"][df1["slopes"]==-1]=0

feature_list = ['kdjk','kdjd','kdjj','macdh','rsi_6','wr_6','wr_10','wr_20',
        'rsi_12','rsi_24']

Y = df1.slopes.values
X = df1[feature_list].values
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.3)


## random forest
clf2 = RandomForestClassifier(n_estimators=100,
        max_depth=None,min_samples_split=2, random_state=0, 
        oob_score=True)
clf2.fit(x_train, y_train)
scores2 = cross_val_score(clf2, x_train, y_train)
print(scores2.mean())

df_feature_importance = pd.DataFrame(clf2.feature_importances_)
df_feature_importance['label'] = feature_list
df_feature_importance.columns = ['importance_score','label']
df_feature_importance.sort_values("importance_score")

df_pred = pd.DataFrame([y_test,clf2.predict(x_test)]).T
df_pred.columns = ["test_true","test_pred"]

df_pred_true = df_pred[df_pred["test_true"] == df_pred["test_pred"]]
df_pred_true.shape[0]/df_pred.shape[0]





## xgboost

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

