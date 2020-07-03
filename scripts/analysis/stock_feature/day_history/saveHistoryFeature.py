from davidyu_cfg import *
#from functions.day_history import dayHistoryFeature.dayHistoryFeature
from functions.day_history.dayHistoryFeature import dayHistoryFeature
from functions.stock_feature.mergeData import mergeData
from sklearn.model_selection import train_test_split
from functions.day_history.rollReg import rollRegDayHis

#rollReg_file = "/home/davidyu/stock/data/tmp_data/stock_feature/rolling_regression/test.csv"
#df_rollReg = pd.read_csv("/home/davidyu/stock/data/tmp_data/stock_feature/rolling_regression/test.csv")

'''
history close as feature
'''
def makeHistoryPriceDF(raw_file,history_days,raw_data_name):
    feature_dir = tmp_data_dict.get("stock_feature")
    save_dir = os.path.join(feature_dir,"HistoryFeature")
    create_dir_if_not_exist(save_dir)
    df_raw = pd.read_csv(raw_file)
    df_history_price = df_raw.groupby('stock_index').apply(lambda x:dayHistoryFeature.make_history_price(x,history_days))
    df3 = df_history_price.reset_index(drop=True)
    insert_colnames = dayHistoryFeature().new_history_days_colname
    df_feature = df3[['stock_index','stock_date']+insert_colnames]
    file_name = "historyPrice_"+raw_data_name
    df_feature.to_csv(os.path.join(save_dir,file_name),index=0)


for i in range(0,20):
    data_dir = os.path.join(tmp_data_dict.get("stock_feature"),"rawData")
    raw_data_name = "history_part%s.csv"%(str(i))
    raw_file = os.path.join(data_dir,raw_data_name)
    history_days = 30
    makeHistoryPriceDF(raw_file,history_days,raw_data_name)

'''
df_feature,insert_colnames = makeHistoryPriceDF(raw_file)


## run to save rolling Regression data
rollReg_file = rollRegDayHis.getRollReg(raw_file,10,'part1.csv')
print(rollReg_file)
df_merge = mergeData(rollReg_file).loadRollingReg().regPN('slopes').mergeWithRollingReg(df_feature).dropna()
#
df_x = df_merge[insert_colnames].values
df_y = df_merge.slopes.values
X_train, X_test, y_train, y_test  = train_test_split(df_x,df_y,
    test_size=0.1, random_state=42)

def LR(X_train, X_test, y_train, y_test):
    from sklearn.linear_model import LogisticRegression

    modelLR = LogisticRegression(C=1000,penalty = 'l2')
    modelLR.fit(X_train,y_train)
    print(modelLR.score(X_test,y_test))

LR(X_train, X_test, y_train, y_test)
from sklearn.preprocessing import StandardScaler
S=StandardScaler()
S.fit(X_train)

x_train_stand=S.transform(X_train)
x_test_stand=S.transform(X_test)

Log=LogisticRegression(C=10)
Log.fit(x_train_stand,y_train) 
print(Log.score(X_test,y_test))

def NB(X_train, X_test, y_train, y_test):
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB().fit(X_train, y_train)
    print(clf.score(X_test,y_test))
'''




