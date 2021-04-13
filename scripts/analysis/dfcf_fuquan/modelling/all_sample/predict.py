import xgboost as xgb
from input_para import *
#from davidyu_cfg import *
#from functions.common.TimeMake import timeFunc
import logging
import pandas as pd

stock_index=sys.argv[1]
pred_days = sys.argv[2]
logging.info("-"*80)

input_data1,feature_columns = get_input_date(stock_index,pred_days)


df1 = pd.read_csv("pred_df.csv")
df1 = df1[["stock_index","dt"]+input_data1.get("feature_columns")].drop_duplicates()
pred_df = df1[input_data1.get("feature_columns")]

xgb_m = xgb.Booster(model_file='all_model.model')
xgb_out = xgb_m.predict(xgb.DMatrix(pred_df)).tolist()

pred_df["stock_index"] = df1["stock_index"]
pred_df["result"] = xgb_out
pred_df["dt"] = df1["dt"]
pred_df = pred_df[["stock_index","result","dt"]+feature_columns]
pred_df1 = pred_df[pred_df["stock_index"]!="stock_index"]
pred_df1.drop_duplicates().sort_values(['stock_index','dt']).round(2).to_csv("predict_out.csv",index=0)
#print(pred_df)
