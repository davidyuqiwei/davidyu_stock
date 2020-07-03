from davidyu_cfg import *
from functions.stock_feature.mergeData import mergeData
from sklearn.feature_selection import SelectKBest,chi2
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel


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


def featureSelectSVC(X,y):
	lsvc = LinearSVC(C=0.0001, penalty="l1", dual=False).fit(X, y)
	df_feature_select = pd.DataFrame(lsvc.coef_).T
	df_feature_select['feature'] = fin_report_df.columns.tolist()[:-1]
	df_feature_select.columns = ["weight","feature"]
	df_fea1 = df_feature_select[df_feature_select["weight"]!=0]
	df_fea2 = df_fea1.sort_values("weight")
	uni_feature = list(set([x.split("_")[0] for x in df_fea1['feature'].tolist()]))
    return df_fea2,uni_feature


from sklearn.linear_model import (RandomizedLasso, lasso_stability_path,
    LassoLarsCV)
import warnings
from sklearn.utils import ConvergenceWarning
with warnings.catch_warnings():
    warnings.simplefilter('ignore', UserWarning)
    warnings.simplefilter('ignore', ConvergenceWarning)
    lars_cv = LassoLarsCV(cv=6).fit(X, y)

alphas = np.linspace(lars_cv.alphas_[0], .1 * lars_cv.alphas_[0], 6)
clf = RandomizedLasso(alpha=alphas, random_state=42).fit(X, y)


model = SelectFromModel(lsvc, prefit=True)
X_new = model.transform(X)
X_new.shape
    
df_merge3.corr(method='pearson')





