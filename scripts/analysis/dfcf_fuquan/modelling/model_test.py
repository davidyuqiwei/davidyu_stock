import lightgbm as lgb
import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle
#X_test = 
with open('X_test.pickle', 'rb') as f: X_test = pickle.load(f)
with open('y_test.pickle', 'rb') as f: y_test = pickle.load(f)
#y_test = pd.read_csv("y_test_data.csv",header=None)

with open('randomF.pickle', 'rb') as f: rf_m = pickle.load(f)  
xgb_m = xgb.Booster(model_file='xgb.model')
lgb_m = lgb.Booster(model_file='lgb.txt')


rf_out = [x[1] for x in rf_m.predict_proba(X_test).tolist()]
xgb_out = xgb_m.predict(xgb.DMatrix(X_test)).tolist()
lgb_out = lgb_m.predict(X_test).tolist()


df_ens_pred = pd.DataFrame()
df_ens_pred["rf_out"] = rf_out
df_ens_pred["xgb_out"] = xgb_out
df_ens_pred["lgb_out"] = lgb_out
df_ens_pred["y_test"] = y_test.values.tolist()                                                                                                                                   

df_ens_pred.to_csv("ensembel_model_result.csv",index=0)



