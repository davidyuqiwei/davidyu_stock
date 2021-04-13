from model.model_read_data import modelData
#from model.modelling import *
#from model.model_para_xgboost import *

data_file = "pred1.csv"
column_names = None

feature_columns = ["rsi_6", "rsi_12","kdjk", "kdjd", "kdjj", "macdh", "boll_ub", "boll_lb"]



y_column = "close"
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


a2 = modelData.get_data(input_data1).set_x_y_column_raw()
X_train, X_test, y_train, y_test = a2.make_train_test_data()

print(X_train)


