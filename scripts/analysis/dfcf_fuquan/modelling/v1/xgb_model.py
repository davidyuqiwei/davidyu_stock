from model.model_read_data import modelData
from model.modelling import *
from model.model_para_xgboost import *
from input_para import *
from davidyu_cfg import *
from functions.common.TimeMake import timeFunc




def get_train_test(stock_index,pred_days):
    input_data1,feature_columns = get_input_date(stock_index,pred_days)
    now_date = timeFunc.getTheDatetime().get("now_date")
    train_end_date = timeFunc.daysAgo(now_date,21)
    a2 = modelData.get_data(input_data1)
    # process the slope column
    a2.DF["slope_cls"] = a2.DF["slopes"]
    a2.DF["slope_cls"][a2.DF["slope_cls"]>0.08]=1
    a2.DF["slope_cls"][a2.DF["slope_cls"]<=0.08]=0
    ## predict data
    pred_df_raw = a2.DF[a2.DF["dt"]>train_end_date]
    pred_df_raw.to_csv("/home/davidyu/stock/data/model/macd_roll_regr_predict_data/pred_df_%s_%s.csv"%(stock_index,pred_days),index=0)
    # train, test data
    a2.DF = a2.DF[a2.DF["dt"]<=train_end_date]
    a2 = a2.set_x_y_column_raw()
    X_train, X_test, y_train, y_test = a2.make_train_test_data()
    return X_train, X_test, y_train, y_test,feature_columns

def train_save_model(X_train, X_test, y_train, y_test,feature_columns):
    ## start run models
    a1 = modelling(X_train, X_test, y_train, y_test)
    model = a1.xgboost(xgboost_para=para_xgboost,xgboost_loop_num=xgboost_loop_num,feature_name=feature_columns)
    model_dir = data_dict.get("model")
    out_model = os.path.join(model_dir,"macd_roll_regr",stock_index+"_xgb_"+"%sdays.model"%pred_days)
    model.get("model").save_model(out_model)
    return a1,model


stock_index=sys.argv[1]
pred_days = sys.argv[2]

logging.info("-"*80)
logging.info(stock_index)
X_train, X_test, y_train, y_test,feature_columns = get_train_test(stock_index,pred_days)
a1,model = train_save_model(X_train, X_test, y_train, y_test,feature_columns)
#print("m1")
m1 = a1.train_predict_df(model)
## model group predict out 
thres = a1.train_cut_score(m1)
logging.info("test data score")
a1.test_score(model.get("model"),y_test,model.get("test_data"), 0.7)

logging.info("-"*80)
logging.info("*"*80)






