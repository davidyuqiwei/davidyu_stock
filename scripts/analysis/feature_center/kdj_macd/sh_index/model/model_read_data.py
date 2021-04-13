import pandas as pd
from sklearn.model_selection import train_test_split
import sys


class modelData:
    data_file = ''
    DF = ''
    feature_columns = ''
    y_column = ''
    df_feature = ''
    test_size = ''
    random_state = ''
    aa = ''

    def __init__(self, **kwargs):
        self.kk = ''

    @classmethod
    def filter_data_a(cls, days=5):
        """
        :param days:  the data combine with the slope, to find
        which slope num wer are interes in this
        :return:
        """
        df2 = cls.DF[cls.DF["slope_num_in"] == days]
        # print(df2[["stock_index", "dt", "slope_num_in"]])
        cls.DF = df2
        return cls

    @classmethod
    def _read_csv(cls, data_file):
        df1 = pd.read_csv(data_file, header=None)
        print(df1.shape)
        if df1.shape[1] < 2:
            df1 = pd.read_csv(data_file, sep="\t", header=None)
            cls.DF = df1
        if df1.shape[0] < 2:
            print("the input dataframe separator is not t or , ")
            sys.exit(2)

        cls.DF = df1
        return cls


    @classmethod
    def get_data(cls, input_data):
        '''

        :param input_data:
        :return:
            data_file = "../data/ttt.csv"
            column_names = ["stock_index", "dt", "slope", "slope_num_in", "days_default", "slope_cls", "slope_cls2", "rsi_6",
                            "rsi_12", "rsi_24", "kdjk", "kdjd", "kdjj", "macdh", "boll_ub", "boll_lb", "boll_ratio"]
            feature_columns = ["rsi_6", "rsi_12", "rsi_24", "kdjk", "kdjd", "kdjj", "macdh", "boll_ub", "boll_lb", "boll_ratio"]
            y_column = "slope_cls"

            input_data1 = {
                "data_file": data_file,
                "column_names": column_names,
                "feature_columns": feature_columns,
                "y_column": y_column
            }
        '''
        data_file = input_data.get("data_file")
        column_names = input_data.get("column_names")
        feature_columns = input_data.get("feature_columns")
        test_size = input_data.get("test_size")
        random_state = input_data.get("random_state")
        y_column = input_data.get("y_column")
        df1 = cls._read_csv(data_file).DF
        if column_names is None:
            column_names = df1.columns
        df1.columns = column_names
        cls.DF = df1
        cls.feature_columns = feature_columns
        cls.DF = df1
        cls.feature_columns = feature_columns
        cls.y_column = y_column
        if test_size is None:
            cls.test_size = 0.2
        else:
            cls.test_size = test_size
        if random_state is None:
            cls.random_state = 1
        else:
            cls.random_state = random_state
        return cls

    @classmethod
    def set_x_y_column(cls):
        df_y = cls.DF[cls.y_column]
        cls.df_feature = cls.DF[cls.feature_columns]
        df_y[df_y == -1] = 0
        cls.df_y = df_y
        return cls

    @classmethod
    def set_x_y_column_raw(cls):
        df_y = cls.DF[cls.y_column]
        cls.df_feature = cls.DF[cls.feature_columns]
        cls.df_y = df_y
        return cls

    @classmethod
    def make_train_test_data(cls):
        print(cls.df_feature.shape)
        X_train, X_test, y_train, y_test = train_test_split(cls.df_feature, cls.df_y,
                                                            test_size=cls.test_size, random_state=cls.random_state)
        return X_train, X_test, y_train, y_test
