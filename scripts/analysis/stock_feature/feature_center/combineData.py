import pandas as pd
from davidyu_cfg import *
from functions.rolling_regression import *
from functions.stock_feature.mergeData import mergeData
from featureConfig import featureConfig
featureDir = ["mvAvg","HistoryFeature","rollRegression"]

feature_dir = tmp_data_dict.get("stock_feature")
featureName = "combineData"
save_dir = featureConfig.makeFeatureSaveDir(featureName)
roll_reg_window = 30

for i in range(0,20):
	raw_data_name,_ = featureConfig().rawDataInfo(i)
	#raw_data_name = "history_part%s.csv"%(str(i))
	## roll regression data
	rollReg_name = "rollRegression_"+str(roll_reg_window)+'_'+raw_data_name
	rollRegFile = os.path.join(feature_dir,"rollRegression",rollReg_name)
	rollRegDf = pd.read_csv(rollRegFile)
	## moving average data
	mvAvgFile = "mvAvg_"+raw_data_name
	mvAvgDf = pd.read_csv(os.path.join(feature_dir,"mvAvg",mvAvgFile))
	## history price data
	historyPriceFile =  "historyPrice_"+raw_data_name
	historyPriceDf = pd.read_csv(os.path.join(feature_dir,"historyPrice",historyPriceFile))
	## dazongjiaoyi  || left join 
	#dazongjiaoyiFile = "dazongjiaoyi_"+raw_data_name
	#dazongjiaoyiDf = pd.read_csv(os.path.join(feature_dir,"dazongjiaoyi",dazongjiaoyiFile))
	####-----------------------------------------------------####
    ####-------------------- merge data ---------------------####
	a1 = pd.merge(rollRegDf,mvAvgDf,on=("stock_date","stock_index"))
	df_model = pd.merge(a1,historyPriceDf)
	df_model = df_model.dropna()
	df_model = mergeData.regPN(df_model,'slopes')
	file_name = featureName+"_"+str(roll_reg_window)+'_'+raw_data_name
	df_model.to_csv(os.path.join(save_dir,file_name),index=0)


#aa =  pd.merge(df_model,dazongjiaoyiDf,how='left',on=("stock_date","stock_index"))
#aa['dazongjiaoyi_cnt'] = aa['dazongjiaoyi_cnt'].fillna(0)
'''
#df_model = df_model[df_model['dazongjiaoyi_cnt']>0]
#df_model = df_model[df_model['stock_date']>'2013-01-01']

feature_cols = np.load("feature_columns.npy").tolist()


df_x = df_model[df_model.columns.intersection(feature_cols)]

df_y = df_model.slopes.values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test  = train_test_split(df_x,df_y,test_size=0.1, random_state=32)
from sklearn.svm import SVC
clf = SVC()
clf.fit(X_train, y_train) 
clf.score(X_test,y_test)

'''




'''
X_train, X_test, y_train, y_test  = train_test_split(df_x,df_y,
    test_size=0.1, random_state=32)


'''



'''
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




from sklearn.naive_bayes import GaussianNB
clf = GaussianNB().fit(X_train, y_train)
clf.score(X_test,y_test)


clf = GaussianNB().fit(x_train_stand, y_train)
clf.score(x_test_stand,y_test)

'''




#clf.fit(x_train_stand, y_train)
#clf.score(x_test_stand,y_test)


'''
from sklearn import linear_model
clf = linear_model.Lasso(alpha=0.01)

clf.fit(x_train_stand,y_train)
clf.score(x_test_stand,y_test)



clf.fit(X_train,y_train)

'''

