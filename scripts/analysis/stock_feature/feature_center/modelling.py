import pandas as pd
from davidyu_cfg import *
from functions.rolling_regression import *
from featureConfig import featureConfig
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

from sklearn.externals import joblib
#featureDir = ["mvAvg","HistoryFeature","rollRegression"]
os.system("rm -rf model_out.txt")
feature_cols = np.load("feature_columns.npy").tolist()
feature_dir = tmp_data_dict.get("stock_feature")
window = 30
loop_range = 9
model_test_loop_range = 100
for loop_i in range(0,model_test_loop_range):
    df1 = pd.DataFrame()
    for i in range(0,loop_range):
        featureName = "combineData"
        save_dir = featureConfig.makeFeatureSaveDir(featureName)
        raw_data_name,_ = featureConfig().rawDataInfo(i)
        file_name = featureName+"_"+str(window)+'_'+raw_data_name
        df_model = pd.read_csv(os.path.join(save_dir,file_name)).sample(frac=0.1)
        df1 = df1.append(df_model)
    df_x = df_model[df_model.columns.intersection(feature_cols)]
    df_y = df_model.slopes.values
    X_train, X_test, y_train, y_test  = train_test_split(df_x,df_y,test_size=0.1, random_state=32)
    ## train model
    clf = SVC()
    clf.fit(X_train, y_train) 
    featureName = "modelOut"
    #loop_i = i
    save_dir = featureConfig.makeFeatureSaveDir(featureName)
    model_name = "svm_model"+str(loop_i)
    save_model = os.path.join(save_dir,model_name)+'.pkl'
    joblib.dump(clf, save_model)
    f2 = open('model_out.txt','a')
    model_score = np.round(clf.score(X_test,y_test),3)
    print(model_score)
    f2.write('\n'+model_name+'\t'+str(model_score))
    f2.close()




'''
pred_test_y = clf.predict(X_test)
m = sm.confusion_matrix(y_test, pred_test_y)

r = sm.classification_report(y_test, pred_test_y)
print('分类报告为 test: ', r, sep='\n')


#### model on predict data
i=loop_range
raw_data_name,_ = featureConfig().rawDataInfo(i)
file_name = featureName+"_"+str(window)+'_'+raw_data_name
df_pred = pd.read_csv(os.path.join(save_dir,file_name)).sample(frac=0.003)

df_predx = df_pred[df_pred.columns.intersection(feature_cols)]
df_predy = df_pred.slopes.values
x_pred = df_predx.values
y_pred =  clf.predict(x_pred)
m = sm.confusion_matrix(y_test, pred_test_y)
r = sm.classification_report(y_pred, df_predy)
print('分类报告为 predict:', r, sep='\n')

'''
import sklearn.metrics as sm


def LR_yu():
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    
    S=StandardScaler()
    S.fit(X_train)
    x_train_stand=S.transform(X_train)
    x_test_stand=S.transform(X_test)
    
    Log = LogisticRegression(C=10)
    Log.fit(x_train_stand,y_train)
    print(Log.score(X_test,y_test))
    print(Log.score(x_test_stand,y_test))






















