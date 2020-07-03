import pandas as pd
from sklearn import svm
from sklearn import linear_model
from sklearn.metrics import explained_variance_score,\
        mean_absolute_error,\
        mean_squared_error,\
        median_absolute_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 

#df1 = pd.read_csv("/home/davidyu/stock/data/test/sample_predNextDayLow.csv",sep="\t")
#df1 = df1.sample(100000)
df1 = pd.read_csv("/home/davidyu/stock/data/test/sample_predNextDayLow_601398.csv",sep="\t")

df1.columns = [x.split(".")[1] for x in df1.columns.tolist()] 
reg = linear_model.LinearRegression(fit_intercept=True,normalize=True)
#stock1 = df1[['today_high','today_low','today_open','today_close','next_low']].dropna()
x = df1[['today_high','today_low','today_open','today_close']].values
y = df1.next_high.values
#reg.fit(x,y)

#X_train, X_test, y_train, y_test  = train_test_split(x,y,test_size=0.3, random_state=32)

def try_different_method(model,X_train,X_test,method=None):
    print(method)
    ss = StandardScaler()
    ss.fit(X_train)
    X_train = ss.transform(X_train)
    X_test = ss.transform(X_test)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score = model.score(X_test, y_test)
    print("mean squared error")
    print(mean_squared_error(y_test,y_pred))
    print("predict r2 score")
    print(r2_score(y_test,y_pred))
    print("median_absolute_error")
    print(median_absolute_error(y_test,y_pred))
    print("explained_variance_score")
    print(explained_variance_score(y_test,y_pred))
    try:
        print(model.coef_)
    except:
        pass
for i in range(0,10):
    X_train, X_test, y_train, y_test  = train_test_split(x,y,test_size=0.9)
    #reg = linear_model.LinearRegression(fit_intercept=True,normalize=False)
    model = linear_model.LinearRegression(fit_intercept=True,normalize=False)
    try_different_method(model,X_train, X_test,"Linear reg")
    print("\n")


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




