import pandas as pd
from davidyu_cfg import *
from functions.rolling_regression import *
from featureConfig import featureConfig
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

from sklearn.externals import joblib
pred_Y = []
predict_prob = []
for i in range(0,100):
    loop_i = i
    window = 30
    featureName = "modelOut"
    save_dir = featureConfig.makeFeatureSaveDir(featureName)
    
    model_name = "svm_model"+str(loop_i)
    save_model = os.path.join(save_dir,model_name)+'.pkl'
    clf = joblib.load(save_model)
    
    i=9
    featureName = "combineData"
    save_dir = featureConfig.makeFeatureSaveDir(featureName)
    raw_data_name,_ = featureConfig().rawDataInfo(i)
    file_name = featureName+"_"+str(window)+'_'+raw_data_name
    #df_pred = pd.read_csv(os.path.join(save_dir,file_name)).iloc[[3000,30000],:]
    df_pred_raw = pd.read_csv(os.path.join(save_dir,file_name))
    df_pred = df_pred_raw[df_pred_raw['slopes']<0].sample(50)
    feature_cols = np.load("feature_columns.npy").tolist()
    df_predx = df_pred[df_pred.columns.intersection(feature_cols)]
    df_predy = df_pred.slopes.values
    x_pred = df_predx.values
    y_pred =  clf.predict(x_pred)
    pred_Y.append(y_pred)
pred_model_df = pd.DataFrame(pred_Y)
aa1 = pred_model_df.replace(-1,0)
aa1.sum()


aa1 = pred_model_df.replace(1,0)
aa1.sum()
#aa1.sum().mean()                                                                         
#69.22



#print(y_pred)
#print(df_predy[0:2])
#pred_prob = len(pred_model_df[pred_model_df[0]==1])/len(pred_model_df)
#predict_prob.append()
#len(pred_model_df[pred_model_df[1]==1])/len(pred_model_df)

#print(pred_model_df.groupby(0).count())
#print(pred_model_df.groupby(1).count())
#m = sm.confusion_matrix(y_test, pred_test_y)
#r = sm.classification_report(y_pred, df_predy)
#print('分类报告为 predict:', r, sep='\n')





