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


df1 = pd.read_csv("/home/davidyu/stock/data/model/macd_roll_regr_predict_data/pred_df_%s_%s.csv"%(stock_index,pred_days))
df1 = df1[["stock_index","dt"]+input_data1.get("feature_columns")].drop_duplicates()
pred_df = df1[input_data1.get("feature_columns")]

xgb_m = xgb.Booster(model_file='/home/davidyu/stock/data/model/macd_roll_regr/%s_xgb_%sdays.model'%(stock_index,pred_days))
xgb_out = xgb_m.predict(xgb.DMatrix(pred_df)).tolist()

pred_df["stock_index"] = stock_index
pred_df["result"] = xgb_out
pred_df["dt"] = df1["dt"]
pred_df["pred_days"] = pred_days
pred_df = pred_df[["stock_index","result","dt","pred_days"]+feature_columns]
pred_df1 = pred_df[pred_df["stock_index"]!="stock_index"]
pred_df1.drop_duplicates().round(2).to_csv("predict_out.csv",index=0,mode="a")
#print(pred_df)
