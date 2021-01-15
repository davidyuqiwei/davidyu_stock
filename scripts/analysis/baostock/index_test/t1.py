from davidyu_cfg import *
import pandas as pd
from functions.common.dfProcess import *
from functions.common.loadModule.load_module_kdj import *
from functions.general.load_model_data import normalizeDf
df1=pd.read_csv("stock_all_close.csv",header=None)
df1.columns = ["stock_index","dt","close"]


df2 = pd.pivot_table(df1,index=["dt"],columns="stock_index",values="close")

mkt_data = pd.read_csv("/home/davidyu/stock/data/test/SH_index_data.csv")
df_sh_index = cleanData.cleanColName(mkt_data)

df_sh_index.index = df_sh_index["stock_date"]
df_sh_close = df_sh_index["close"]

df = pd.merge(df2,df_sh_close,left_index=True,right_index=True)
df3 = df.dropna(axis=1, how='any')
df_data = normalizeDf(df3).normDF()
df_data = df_data.dropna(axis=1, how='any')
# df_data.iloc[:,370:400] 


from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

X_train = np.round(df_data.drop(columns = ["close"]).values,3)+0.001
y_train = np.round(df_data["close"].values,3)+0.001

model = XGBClassifier()
model.fit(X_train, y_train)
model.predict()

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_regression

fs = SelectKBest(score_func=chi2, k=10)
fit = fs.fit(X_train,y_train)

dfscores = pd.DataFrame(fit.scores_)
#create df for column names
dfcolumns = pd.DataFrame(df_data.drop(columns = ["close"]).columns)
#concat two dataframes for better visualization 
featureScores = pd.concat([dfcolumns,dfscores],axis=1)
#naming the dataframe columns
featureScores.columns = ['Selected_columns','Score_pearsons']

featureScores.sort_values("Score_pearsons").tail(10)

