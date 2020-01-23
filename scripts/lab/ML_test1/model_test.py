import pickle
from sklearn.externals import joblib
import random
import numpy as np
pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
x_test = data1['x_test']
y_test = data1['y_test']
clf = joblib.load("svm_train_model_raw_scale.m")
def model_test(clf,x_test,y_test):
    model_fit = []
    for i in range(100):
        rand_ind = [random.randint(0,x_test.shape[0]-1) for _ in range(50)]
        y_predict = clf.predict(x_test[rand_ind])
        y_raw = y_test[rand_ind]
        a1 = y_raw-y_predict
        fit_ratio = len(a1[a1==0])/50
        #print(fit_ratio)
        model_fit.append(fit_ratio)
    print(np.mean(model_fit))

model_test(clf,x_test,y_test)


