from model_read_data import *
from modelling import * 
#from model_para_xgboost import *
from sklearn.metrics import accuracy_score
from m_features import *
from model_para_xgboost_multi import *
# data_file = "../data/ttt.csv"
#data_file = "/home/davidyu/stock/data/test/dfcf_fuquan_kdj_reg.csv"
data_file = "/home/davidyu/stock/data/test/dfcf_fuquan_kdj_reg_add_mv_avg.csv"
column_names = ["stock_index", "dt", "slope", "slope_num_in", "days_default", "slope_cls", "slope_cls2","slope_cls3", "rsi_6",
                "rsi_12", "rsi_24", "kdjk", "kdjd", "kdjj", "macdh", "boll_ub", "boll_lb", "boll_ratio",
                "mv_avg_3_5","mv_avg_3_8","mv_avg_3_13","mv_avg_5_8",
                "close_mvavg3",
                "close_mvavg5",
                "close_mvavg8",
                "close_mvavg13",
                "close_mvavg21",
                "high_mvavg3",
                "high_mvavg5",
                "high_mvavg8",
                "high_mvavg13",
                "high_mvavg21",
                "low_mvavg3",
                "low_mvavg5",
                "low_mvavg8",
                "low_mvavg13",
                "low_mvavg21",
                "open_mvavg5",
                "open_mvavg8",
                "open_mvavg13",
                "open_mvavg21"]



y_column = "slope_cls3"
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

a2 = modelData.get_data(input_data1).filter_data_a(5).set_x_y_column3()
X_train, X_test, y_train, y_test = a2.make_train_test_data()
a1 = modelling(X_train, X_test, y_train, y_test).StandardData()
#X_test.to_csv("x_test_data.csv",index=0)
#y_test.to_csv("y_test_data.csv",index=0)

model_run = 'xgb'  ## xgb,lgb,randomF
## xgboost
if model_run == 'xgb':
    dd = a1.xgboost(xgboost_para=para_xgboost,xgboost_loop_num=xgboost_loop_num,feature_name=feature_columns)
    xgboost_model = dd.get("model").save_model('xgb_index_base_multi.model')
    '''
    m1 = a1.train_predict_df(dd)
    thres = a1.train_cut_score(m1)
    a1.test_score(dd.get("model"),y_test, dd.get("test_data"), thres)
    a1.test_score(dd.get("model"),y_test, dd.get("test_data"), 0.7)
    a1.test_score(dd.get("model"),y_test, dd.get("test_data"), 0.75)
    a1.test_score(dd.get("model"),y_test, dd.get("test_data"), 0.8)
    a1.test_score(dd.get("model"),y_test, dd.get("test_data"), 0.85)
    #a1.test_score(dd.get("model"),y_test, dd.get("test_data"), 0.9)
    
    pred_df = X_test
    pred_df["y_obs"] = a1.test_score(dd.get("model"),y_test, dd.get("test_data"), 0.8)["obs_test"].values.tolist()
    pred_df["pred_test"] = a1.test_score(dd.get("model"),y_test, dd.get("test_data"), 0.8)["pred_test"].values.tolist()
    
    df_error = pred_df[(pred_df["y_obs"]==0)&(pred_df["pred_test"]>0.692)]
    df_error["slope"] = a2.DF["slope"].reindex(df_error.index.tolist())

    '''
    
    #df_error.to_csv("error"+str(random_state)+".csv",index=0)
    

# lightgbm
if model_run == 'lgb':
    model_out = a1.StandardData().lightgbm()
    train_pred_df = a1.train_predict_df(model_out)
    print(train_pred_df)
    thres = a1.train_cut_score(train_pred_df)
    a1.test_score(model_out.get("model"),y_test, model_out.get("test_data"), thres)
    model_out.get("model").save_model("lgb.txt")


# random Forest
if model_run == 'randomF':
    import pickle
    #from sklearn.externals import joblib
    model_out = a1.StandardData().randomF()
    with open('X_test.pickle', 'wb') as f: pickle.dump(a1.X_test, f)
    with open('y_test.pickle', 'wb') as f: pickle.dump(a1.y_test, f)
    train_pred_df = a1.train_predict_df(model_out,model_type=2)
    print(train_pred_df)
    #print(train_pred_df.sum())
    thres = a1.train_cut_score(train_pred_df,2)
    pred_df1 = a1.test_score(model_out.get("model"),y_test, model_out.get("test_data"), 0.8,2)
    #joblib.dump(model_out.get("model"),'randomF.pkl')
    with open('randomF.pickle', 'wb') as f: pickle.dump(model_out.get("model"), f)


# lstm
if model_run == "lstm":
    from lstm_model import *
    dl_model = DL_model(a1.X_train,a1.X_test,a1.y_train.values,a1.y_test).load_model3()

    model_out = dl_model.model
    model_out.fit(dl_model.X_train,dl_model.y_train,epochs=2, batch_size=30, verbose=1,validation_split=0.2)
    y_predict = model_out.predict(dl_model.X_test)

if model_run == "dense":
    from lstm_model import *
    dl_model = DL_model(a1.X_train,a1.X_test,a1.y_train.values,a1.y_test).load_model4()
    model_out = dl_model.model
    model_out.fit(a1.X_train,dl_model.y_train,epochs=20, batch_size=128, verbose=1,validation_split=0.2)
    
    y_predict = model_out.predict(a1.X_train)
    pred_df1 = pd.DataFrame()
    pred_df1["slope_cls"] = y_train.values.tolist()
    pred_df1["pred"] = [x[0] for x in y_predict]
    #print(pred_df1.sort_values("y_pred",ascending=False))
    thres = a1.train_cut_score(pred_df1,1)

    print("predict data")
    y_predict = model_out.predict(a1.X_test)
    pred_df1 = pd.DataFrame()
    pred_df1["slope_cls"] = y_test.values.tolist()
    pred_df1["pred"] = [x[0] for x in y_predict]
    #print(pred_df1.sort_values("y_pred",ascending=False))
    thres = a1.train_cut_score(pred_df1,1)


# LR 
if model_run == "LR":
	dd = a1.StandardData().LR()
	bst = dd.get("model")
	b1 = bst.predict(dd.get("train_data"))
	train_acc = round(accuracy_score(y_train,b1),4)
	print(train_acc)
	
	
	
	predict_test = bst.predict(X_test)
	test_acc1 = round(accuracy_score(y_test,predict_test),4)
	print(test_acc1)




