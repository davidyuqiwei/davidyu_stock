from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import xgboost as xgb
class davidCluster:
    def __init__(self,x_train, y_train,x_test,y_test):
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test 
        self.y_test = y_test
        self.y_predict = 0
        self.cross_val_score = 0
        self.model = ""
    def RandomForestClassifier(self):
        ## random forest
        clf2 = RandomForestClassifier(n_estimators=100,
                max_depth=None,min_samples_split=2, random_state=0,
                oob_score=True)
        clf2.fit(self.x_train, self.y_train)
        self.cross_val_score = cross_val_score(clf2, self.x_train, self.y_train)
        self.y_predict = clf2.predict(self.x_test)
        self.model = clf2
        return self
    def xgBoost(self):
        #booster:
        params={'booster':'gbtree',
                'objective': 'binary:logistic',
                'eval_metric': 'auc',
                'max_depth':7,
                'lambda':15,
                'subsample':0.75,
                'colsample_bytree':0.75,
                'min_child_weight':1,
                'eta': 0.025,
                'seed':0,
                'nthread':8,
                'silent':1,
                'gamma':0.15,
                'learning_rate' : 0.05}
        dtrain = xgb.DMatrix(self.x_train,label=self.y_train)
        dtest = xgb.DMatrix(self.x_test)
        watchlist = [(dtrain,'train')]
        bst = xgb.train(params,dtrain,num_boost_round=100,evals=watchlist)
        y_predict = bst.predict(dtest)
        self.y_predict = (y_predict >= 0.5)*1
        return self
    def printModelResult(self):
        #print(self.scores2.mean())
        print('准确率', metrics.accuracy_score(self.y_test, self.y_predict))
        print('平均f1-score:', metrics.f1_score(self.y_test,self.y_predict, average='weighted'))
        #self.model.feature_importances_
