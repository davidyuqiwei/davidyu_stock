from davidyu_cfg import *
from functions.stock_feature.mergeData import mergeData
from sklearn.feature_selection import SelectKBest,chi2
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import Imputer
#https://www.jianshu.com/p/b3056d10a20f


tmp_data_dir = tmp_data_dict.get("financial_report")
df_merge3 = pd.read_csv(os.path.join(tmp_data_dir,"financial_report_ml_test_data.csv"))
df_merge3 = df_merge3.replace(-9999,np.nan) ## 180

def df_corr():
    ## calculate the correlation of all the fin report index
    df_merge3.corr(method='pearson')['change_rate'].sort_values()


## transform data for feature selection
X = df_merge3[df_merge3.columns.tolist()[:-1]].values
imp = Imputer(missing_values=np.nan , strategy='mean', axis=0)
#imp.fit(X)
X = imp.fit_transform(X)
#y = df_merge3['change_rate'].values
df_y = mergeData.regPN(df_merge3,"change_rate")
y = df_y['change_rate']

## 正则化 ， featureSelection
def featureSelectSVC(X,y):
    lsvc = LinearSVC(C=0.0001, penalty="l1", dual=False).fit(X, y)
    df_feature_select = pd.DataFrame(lsvc.coef_).T
    df_feature_select['feature'] = df_merge3.columns.tolist()[:-1]
    df_feature_select.columns = ["weight","feature"]
    df_fea1 = df_feature_select[df_feature_select["weight"]!=0]
    df_fea2 = df_fea1.sort_values("weight")
    uni_feature = list(set([x.split("_")[0] for x in df_fea1['feature'].tolist()]))
    return df_fea2,uni_feature

df_fea2,uni_feature = featureSelectSVC(X,y)
print(uni_feature)


## RandomizedLasso, feature stability selection 
from sklearn.linear_model import (RandomizedLasso, lasso_stability_path,
    LassoLarsCV)
import warnings
from sklearn.exceptions import ConvergenceWarning

with warnings.catch_warnings():
    warnings.simplefilter('ignore', UserWarning)
    warnings.simplefilter('ignore', ConvergenceWarning)
    lars_cv = LassoLarsCV(cv=6).fit(X, y)


alphas = np.linspace(lars_cv.alphas_[0], .1 * lars_cv.alphas_[0], 6)
clf = RandomizedLasso(alpha=alphas, random_state=42).fit(X, y)
names = df_merge3.columns.tolist()[:-1]
print(sorted(zip(map(lambda x: round(x, 4), clf.scores_), 
    names), reverse=True))




from sklearn.ensemble import ExtraTreesClassifier
clf = ExtraTreesClassifier()
clf = clf.fit(X, y)
df_tree = pd.DataFrame(clf.feature_importances_)
df_tree['fea_index'] =  df_merge3.columns.tolist()[:-1]
df_tree.columns = ["weight","feature_index"]
df_tree.sort_values("weight").tail(10)



#model = SelectFromModel(lsvc, prefit=True)
#X_new = model.transform(X)
#X_new.shape
    





