#import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.linear_model import LinearRegression, SGDRegressor, LogisticRegression
from sklearn import svm
#import lightgbm as lgb
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
import pickle
class modelling:
    def __init__(self, X_train, X_test, y_train, y_test, **kwargs):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test

        # xgboost parameter
        input_para = kwargs

    def StandardData(self):
        ss = StandardScaler()
        self.X_train = ss.fit_transform(self.X_train)
        with open('scaler.pickle', 'wb') as f: pickle.dump(ss, f)
        self.X_test = ss.transform(self.X_test)
        return self

    def xgboost(self,**kwargs):
        import xgboost as xgb
        input_para = kwargs
        xgboost_para = input_para.get("xgboost_para")
        xgboost_loop_num = input_para.get("xgboost_loop_num")
        feature_name = input_para.get("feature_name")
        

        print("run xgboost")
        dtrain = xgb.DMatrix(self.X_train, label=self.y_train)
        dtest = xgb.DMatrix(self.X_test)
        if xgboost_para is not None:
            params = xgboost_para
        else:
            params = xgboost_para = {'booster': 'gbtree',
                                          'objective': 'binary:logistic',
                                          'eval_metric': 'auc',
                                          'max_depth': 7,
                                          'lambda': 15,
                                          'subsample': 0.75,
                                          'colsample_bytree': 0.75,
                                          'min_child_weight': 1,
                                          'eta': 0.025,
                                          'seed': 0,
                                          'nthread': 8,
                                          'silent': 1,
                                          'gamma': 0.15,
                                          'learning_rate': 0.1
                                          }
        watchlist = [(dtrain, 'train')]
        if xgboost_loop_num is not None:
            num_boost_round = xgboost_loop_num
        else:
            num_boost_round = xgboost_loop_num = 100
        bst = xgb.train(params, dtrain, num_boost_round=num_boost_round, evals=watchlist)
        feature_import = pd.DataFrame(bst.get_fscore(), index=[0]).T.reset_index()
        feature_import.columns = ["feature_name", "score"]
        feature_import["feature_name"] = feature_name
        print("num_boost_round: " + str(num_boost_round))
        print("feature importance")
        print(feature_import.sort_values("score", ascending=False))

        return_data = {
            'model': bst,
            'train_data': dtrain,
            'test_data': dtest
        }
        return return_data

    def LR(self):
        lg = LogisticRegression(C=0.5)
        lg.fit(self.X_train, self.y_train)
        return_data = {
            'model': lg,
            'train_data': self.X_train,
            'test_data': self.X_test
        }
        return return_data

    def svm(self):
        clf = svm.SVC()
        clf.fit(self.X_train, self.y_train)
        return_data = {
            'model': clf,
            'train_data': self.X_train,
            'test_data': self.X_test
        }
        return return_data

    def lightgbm(self):
        import lightgbm as lgb
        lgb_train = lgb.Dataset(self.X_train, label=self.y_train)
        lgb_eval = lgb.Dataset(self.X_test, label=self.y_test)

        params = {
            'task': 'train',
            'boosting_type': 'gbdt',  # 设置提升类型
            'objective': 'binary',  # 目标函数
            'metric': {'l2', 'auc'},  # 评估函数
            'num_leaves': 31,  # 叶子节点数
            'learning_rate': 0.1,  # 学习速率
            'feature_fraction': 0.7,  # 建树的特征选择比例
            'bagging_fraction': 0.8,  # 建树的样本采样比例
            'bagging_freq': 5,  # k 意味着每 k 次迭代执行bagging
            'verbose': 1,  # <0 显示致命的, =0 显示错误 (警告), >0 显示信息
            'max_depth': -10,
            'learning_rate':0.01
        }

        print('Start training...')
        # 训练 cv and train
        gbm = lgb.train(params, lgb_train, num_boost_round=500, valid_sets=lgb_eval,
                        early_stopping_rounds=20)  # 训练数据需要参数列表和数据集
        return_data = {
            'model': gbm,
            'train_data': self.X_train,
            'test_data': self.X_test
        }
        return return_data
    def randomF(self):
        clf2 = RandomForestClassifier(n_estimators=60,max_features='sqrt',min_samples_split=30, bootstrap=True,
                max_depth=10,)
        clf2.fit(self.X_train, self.y_train)
        return_data = {
            'model': clf2,
            'train_data': self.X_train,
            'test_data': self.X_test
        }
        f1 = pd.DataFrame(self.feature_name)
        f1["score"] = clf2.feature_importances_
        f1.columns = ["feature_name", "score"]
        f2 = f1.sort_values("score", ascending=False)
        print("feature importance")
        print(f2)
        return return_data
        
    def train_predict_df(self, model_out,model_type=1):
        '''
        xgboost predict model train
        :param model_out:
        :return:
        '''
        model_train = model_out.get("model")
        if model_type !=1:
            pred_y = model_train.predict_proba(model_out.get("train_data"))
            pred_y = [x[1] for x in pred_y.tolist()]
        else:
            pred_y = model_train.predict(model_out.get("train_data"))
            pred_y = [np.round(x, 3) for x in pred_y.tolist()]

        train_pred_df = pd.DataFrame(self.y_train.values.tolist())
        train_pred_df["pred"] = pred_y
        train_pred_df.columns = ["slope_cls", "pred"]
        return train_pred_df

    @staticmethod
    def train_cut_score(b2,quant_set=1):
        if quant_set==1:
            d_bins = b2["pred"].quantile([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.98, 0.99])
        else:
            d_bins = b2["pred"].quantile([0.1,  0.3, 0.5,  0.7,  0.9])
        d_bins1 = [x + np.float(np.random.rand(1) * 0.001) for x in d_bins.values.tolist()]
        groups = pd.cut(b2['pred'], bins=[0] + d_bins1 + [1])
        b2["groups"] = groups

        b3 = b2.groupby("groups").sum()["slope_cls"].reset_index()
        b3["count"] = b2.groupby("groups").count()["slope_cls"].values.tolist()
        b3["pos_ratio"] = b3["slope_cls"] / b3["count"]
        print("group prediction score")
        print(b3)
        thres = b2["pred"].quantile(0.98)
        print("threshold: " + str(np.round(thres, 3)))
        return thres

    @staticmethod
    def test_score(bst, y_test, dtest, thres,model_type=1):
        if model_type !=1:
            pred_y = bst.predict_proba(dtest)
            ypred = [x[1] for x in pred_y.tolist()]
        else:
            ypred = bst.predict(dtest).tolist()
        df_pred_raw = pd.DataFrame(ypred,y_test.tolist()).reset_index()
        df_pred_raw.columns = ["obs_test", "pred_test"]
        x = df_pred_raw.copy()
        df_pred = x.loc[x["pred_test"]>thres,:]
        # thres = df_pred["pred_test"].quantile(0.98)
        df_pred["pred_test"][df_pred["pred_test"] > thres] = 1
        df_pred["pred_test"][df_pred["pred_test"] <= thres] = 0
        #pred_ratio = df_pred[df_pred["pred_test"] == df_pred["obs_test"]].shape[0] / df_pred.shape[0]
        pos_ratio = df_pred[df_pred["obs_test"] == 1].sum()[1] / df_pred.shape[0]
        print("pred postive ratio: " + str(np.round(pos_ratio, 3)))
        return df_pred_raw

if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    from model.model_para_xgboost import *

    d = {'col1': np.random.randn(1000).tolist(), 'col2': np.random.randn(1000).tolist()}
    df = pd.DataFrame(data=d)
    df_y = df["col2"]
    df_y[df_y == -1] = 0
    df_y[df_y < 0] = 0
    df_y[df_y > 0] = 1

    X_train, X_test, y_train, y_test = train_test_split(df, df["col2"],
                                                        test_size=0.1, random_state=2)
    print(X_train)
    a1 = modelling(X_train, X_test, y_train, y_test, xgboost_para=para_xgboost)
    # a1.X_train
    dd = a1.StandardData().xgboost()
    # print(a1.xgboost_loop_num)

    thres = a1.train_cut_score(dd.get("model"), y_train, dd.get("train_data"))
    a1.test_score(dd.get("model"), y_test, dd.get("test_data"), thres)

