import sys
#stock_index=sys.argv[1]
#data_file = "/home/davidyu/stock/data/test/%s_macd_slope.csv"%stock_index

def get_input_date(stock_index,pred_days=3):
    if pred_days == "3":
        data_file = "/home/davidyu/stock/data/feature_center/combine_data/%s_macd_slope3.csv"%stock_index
    if pred_days == "5":
        data_file = "/home/davidyu/stock/data/feature_center/combine_data/%s_macd_slope5.csv"%stock_index

    data_file = "/home/davidyu/stock/data/test/xgb_test_data.csv"
    feature_columns = ["rsi_6", "rsi_12", "rsi_24", "kdjk", "kdjd", "kdjj","cci","wr_6"]
    
    y_column = "slopes"
    test_size = 0.2
    random_state = 5
    
    input_data1 = {
        "data_file": data_file,
        "column_names": None,
        "feature_columns": feature_columns,
        "y_column": "slope_cls",
        'test_size': test_size,
        'random_state': random_state
    }
    return input_data1,feature_columns
