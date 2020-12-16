from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import xgboost as xgb
from sklearn.model_selection import GridSearchCV
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
    def xgBoost(self,params):
        #booster:
        if params != "test":
	        params={'booster':'gbtree',
	                'objective': 'binary:logistic',
	                'eval_metric': 'rmse',
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
	                'learning_rate' : 0.05,
	                'silent':True}
        dtrain = xgb.DMatrix(self.x_train,label=self.y_train)
        dtest = xgb.DMatrix(self.x_test)
        watchlist = [(dtrain,'train')]
        bst = xgb.train(params,dtrain,num_boost_round=600,evals=watchlist)
        y_predict = bst.predict(dtest)
        self.y_predict = y_predict
        return self
    def xgbGridClssifer(self):
        parameters = {
              'max_depth': [5, 25],
              'learning_rate': [0.01, 0.15],
              'n_estimators': [500,  5000],
              'min_child_weight': [2, 20],
              'subsample': [0.6, 0.95],
              'colsample_bytree': [0.5, 0.9],
              'reg_alpha': [0, 0.75],
              'reg_lambda': [0.2,  0.8],
              'scale_pos_weight': [0.2,  0.8]
         }
        xlf = xgb.XGBClassifier(max_depth=10,
            learning_rate=0.01,
            n_estimators=2000,
            silent=True,
            objective='binary:logistic',
            nthread=-1,
            gamma=0,
            min_child_weight=1,
            max_delta_step=0,
            subsample=0.85,
            colsample_bytree=0.7,
            colsample_bylevel=1,
            reg_alpha=0,
            reg_lambda=1,
            scale_pos_weight=1,
            seed=1440,
            missing=None)
            
        # 有了gridsearch我们便不需要fit函数
        gsearch = GridSearchCV(xlf, param_grid=parameters, scoring='accuracy', cv=3)
        gsearch.fit(self.x_train, self.y_train)
        print("Best score: %0.3f" % gsearch.best_score_)
        print("Best parameters set:")
        best_parameters = gsearch.best_estimator_.get_params()
        for param_name in sorted(parameters.keys()):
            print("\t%s: %r" % (param_name, best_parameters[param_name]))
    def printModelResult(self):
        #print(self.scores2.mean())
        print('准确率', metrics.accuracy_score(self.y_test, self.y_predict))
        print('平均f1-score:', metrics.f1_score(self.y_test,self.y_predict, average='weighted'))
        #self.model.feature_importances_
