from davidyu_cfg import *
from functions.stock_feature.mergeData import mergeData
from sklearn.feature_selection import SelectKBest,chi2
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel
from sklearn.decomposition import PCA
from sklearn.preprocessing import Imputer

tmp_data_dir = tmp_data_dict.get("financial_report")
df_merge3 = pd.read_csv(os.path.join(tmp_data_dir,"financial_report_ml_test_data.csv"))
df_merge3 = df_merge3.replace(-9999,np.nan)


select_col = [x for x in df_merge3.columns if "12-31" in x] 


x = df_merge3[select_col].values

## process NA value
imp = Imputer(missing_values=np.nan , strategy='mean', axis=0)
X = imp.fit_transform(x)


pca = PCA(n_components=3)
pca.fit(X)

df1 = pd.DataFrame(df_merge3[select_col].columns.tolist(),pca.components_[0].tolist()).reset_index()
df1.columns = ["weight","label"]
df1.sort_values("weight")




