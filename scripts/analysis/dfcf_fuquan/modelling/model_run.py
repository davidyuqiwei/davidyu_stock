from model_read_data import *
from modelling import * 
from model_para_xgboost import *
from sklearn.metrics import accuracy_score

# data_file = "../data/ttt.csv"
data_file = "/home/davidyu/stock/data/test/dfcf_fuquan_kdj_reg.csv"
column_names = ["stock_index", "dt", "slope", "slope_num_in", "days_default", "slope_cls", "slope_cls2", "rsi_6",
                "rsi_12", "rsi_24", "kdjk", "kdjd", "kdjj", "macdh", "boll_ub", "boll_lb", "boll_ratio"]
feature_columns = ["rsi_6", "rsi_12", "rsi_24", "kdjk", "kdjd", "kdjj", "macdh", "boll_ub", "boll_lb", "boll_ratio"]


y_column = "slope_cls"
test_size = 0.2
random_state = 5


input_data1 = {
    "data_file": data_file,
    "column_names": column_names,
    "feature_columns": feature_columns,
    "y_column": y_column,
    'test_size': test_size,
    'random_state': random_state
}

a2 = modelData.get_data(input_data1).filter_data_a(5).set_x_y_column()
X_train, X_test, y_train, y_test = a2.make_train_test_data()

a1 = modelling(X_train, X_test, y_train, y_test, xgboost_para=para_xgboost,xgboost_loop_num=xgboost_loop_num,feature_name=feature_columns)
## xgboost
'''
dd = a1.StandardData().xgboost()
thres = a1.train_cut_score(dd.get("model"), y_train, dd.get("train_data"))
a1.test_score(dd.get("model"),y_test, dd.get("test_data"), thres)

'''

# lightgbm
model_out = a1.StandardData().lightgbm()
train_pred_df = a1.train_predict_df(model_out)
print(train_pred_df)
thres = a1.train_cut_score(train_pred_df)
a1.test_score(model_out.get("model"),y_test, model_out.get("test_data"), thres)





# LR 
'''
dd = a1.StandardData().LR()
bst = dd.get("model")
b1 = bst.predict(dd.get("train_data"))
train_acc = round(accuracy_score(y_train,b1),4)
print(train_acc)



predict_test = bst.predict(X_test)
test_acc1 = round(accuracy_score(y_test,predict_test),4)
print(test_acc1)

'''



