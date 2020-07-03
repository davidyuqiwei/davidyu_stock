import pandas as pd
from sklearn import svm
from sklearn import linear_model
from sklearn.metrics import explained_variance_score,\
        mean_absolute_error,\
        mean_squared_error,\
        median_absolute_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from davidyu_cfg import *
from functions.pyspark_functions import *

class dayHistoryDataSample:
    @staticmethod
    def getPredNextLowData(stock_index):
        sql1 = """
        select a.stock_date as today,
        b.stock_date as next_day,
        a.stock_index,
        a.low*a.adj_close/a.close as today_low,
        a.high*a.adj_close/a.close as today_high,
        a.close*a.adj_close/a.close as today_close,
        a.open*a.adj_close/a.close as today_open,
        b.low*a.adj_close/a.close as next_low,
        b.high*a.adj_close/a.close as next_high
        from
        stock_dev.day_history_insert a
        left join
        (
            select stock_date,stock_index,low,high
            from stock_dev.day_history_insert
        ) b
        on a.stock_index = b.stock_index and datediff(b.stock_date,a.stock_date)=1
        where b.stock_date is not null and a.stock_index='%s'
        order by rand()
        """%(stock_index)
        return sql1



def try_different_method(model,X_train,X_test,method=None):
    #print(method)
    '''
    ss = StandardScaler()
    ss.fit(X_train)
    X_train = ss.transform(X_train)
    X_test = ss.transform(X_test)

    '''
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score = model.score(X_test, y_test)
    median_absolute_err = median_absolute_error(y_test,y_pred)
    mean_squared_err = mean_squared_error(y_test,y_pred)
    pred_error = y_test-y_pred
    gt_real = len(np.where(pred_error>0)[0])
    lt_real = len(np.where(pred_error<0)[0])
    '''
    print("mean squared error")
    print(mean_squared_error(y_test,y_pred))
    print("predict r2 score")
    print(r2_score(y_test,y_pred))
    print("median_absolute_error")
    print(median_absolute_error(y_test,y_pred))
    print("explained_variance_score")
    print(explained_variance_score(y_test,y_pred))
    '''
    try:
        #print(model.coef_)
        2+3
    except:
        pass
    return median_absolute_err,mean_squared_err,model.coef_,gt_real,lt_real
df_raw = spark.sql(dayHistoryDataSample.getPredNextLowData('601899'))
df1 = df_raw.toPandas().round(2)
reg = linear_model.LinearRegression(fit_intercept=True,normalize=True)
x = df1[['today_high','today_low','today_open','today_close']].values
y = df1.next_low.values

median_absolute_err_list = []
coef_list = []
mean_squared_err_list = []
gt_real_list = []
lt_real_list = []
for i in range(0,1000):
    X_train, X_test, y_train, y_test  = train_test_split(x,y,test_size=0.1)
    #reg = linear_model.LinearRegression(fit_intercept=True,normalize=False)
    model = linear_model.LinearRegression(fit_intercept=True,normalize=False)
    median_absolute_err,mean_squared_err,coef,gt_real,lt_real = try_different_method(model,X_train, X_test,"Linear reg")
    median_absolute_err_list.append(np.round(median_absolute_err,3))
    coef_list.append(np.round(coef,4))
    mean_squared_err_list.append(np.round(mean_squared_err,3))
    gt_real_list.append(gt_real)
    lt_real_list.append(lt_real)
df_reg_out = pd.DataFrame([coef_list,median_absolute_err_list,\
        mean_squared_err_list,gt_real_list,lt_real_list]).T
df_reg_out.columns = ['coefs','median_absolute_err','mean_squared_err',"gt_real_list","lt_real_list"]
df_reg_out.sort_values("median_absolute_err").to_csv("pred.csv",index=0)
#print(df_reg_out.sort_values("median_absolute_err").head(20))
'''
## 已经测试，线性回归最好
model = svm.SVR()
try_different_method(model,X_train, X_test,"SVR")

from sklearn import tree
model_decision_tree_regression = tree.DecisionTreeRegressor()

try_different_method(model_decision_tree_regression,X_train, X_test,"decision_tree_regression ")

from sklearn import ensemble
model_gradient_boosting_regressor = ensemble.GradientBoostingRegressor(n_estimators=100) 
try_different_method(model_gradient_boosting_regressor,X_train, X_test,"gradient_boosting_regressor")

'''




