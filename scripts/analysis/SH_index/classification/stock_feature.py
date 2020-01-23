from load_model_data import *
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import featuretools as ft
from feature_functions import *
def load_data():
    data_dir = "/home/davidyu/stock/data/test/for_lstm"
    file_name = "SH_index.csv"
    df1 = read_mv_avg_data_clean(data_dir,file_name)
    history_days = 30
    #
    df1 = make_history_price(df1,history_days)
    df1 = make_history_vol(df1,history_days)
    df1 = df1.drop(columns=['volume'])
    return df1


#df1.drop(df1.columns[[0,1,2]], axis=1, inplace=True)

def make_input_data():
    df1 = load_data()
    #y_raw = [1 if x>0 else 0 for x in df1.adj_close.diff().tolist() ]
    start_index = 1980
    df1 = df1[start_index:]
    df1 = df1.sample(frac=1)
    fea_col = feature_columns()  ## which columns are used for make features
    feature_matrix,feature_names = make_features(df1,fea_col)
    feature_matrix.drop(columns=fea_col[1:],inplace=True)  ## drop the first columns, 'index' used formake features
    x_raw = feature_matrix.values
    y_raw = [1 if x>0 else 0 for x in df1.adj_close.diff().tolist() ]  ## 1: increase ,,  0 : decrease
    #df_X = feature_matrix.drop(columns=fea_col[1:],inplace=True)
    #df1.drop(df1.columns[[0,1,2]],axis=1, inplace=True)
    #df1.drop(df1.columns[[1,2]],axis=1, inplace=True)
    #df1 = df1[df1.columns[[0,3,4,5,6]]]
    return x_raw,y_raw,feature_matrix,feature_names


#x_raw = normalize_DF(df1)
def make_train_test_pred_data(x_raw,y_raw):
    y_raw = np.array(y_raw)
    data_len = x_raw.shape[0]
    train_index = int(data_len*0.7)
    test_index = train_index + int(data_len*0.2)
    predict_index = data_len
    x_input1 = x_raw[0:train_index]
    y_input1 = y_raw[0:train_index]
    train_X = x_input1
    train_y = y_input1
    test_X = x_raw[train_index:test_index]
    test_y = y_raw[train_index:test_index]
    pred_x = x_raw[test_index:predict_index]
    pred_y = y_raw[test_index:predict_index]
    return train_X,train_y,test_X,test_y,pred_x,pred_y

x_raw,y_raw,feature_matrix,feature_names = make_input_data()

train_X,train_y,test_X,test_y,pred_x,pred_y = make_train_test_pred_data(x_raw,y_raw)

model_tree = DecisionTreeClassifier(max_depth=5,min_samples_split=2,random_state=0)

model_tree.fit(train_X, train_y)
model_score = model_tree.score(train_X, train_y)
print('DT Model Accuracy: %.2f'%model_score)

data_dict = {
    'feature_name':feature_matrix.columns.values,
    'feature_score': model_tree.feature_importances_

        }
df_fea_imp = pd.DataFrame(data_dict)
df_fea_imp = df_fea_imp.sort_values("feature_score",ascending=False)

import graphviz
import pydotplus
from sklearn import tree

data_feature_name = [x.replace("<","less") for x in feature_matrix.columns.values]
#data_target_name = [str(x) for x in y_raw]
data_target_name = ["0","1"]
dot_tree = tree.export_graphviz(model_tree,out_file=None,feature_names=data_feature_name,class_names=data_target_name,filled=True, rounded=True,special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_tree)
#img = Image(graph.create_png())
graph.write_png("out.png")

pred_y = model_tree.predict(test_X)

pred_correct_ratio = 1-sum(np.abs(pred_y - test_y))/len(test_y)
print('DT Correct ratio on test data: %.2f'%pred_correct_ratio)



df2 = feature_matrix['mv_avg300 < mv_avg120']
df2 = pd.DataFrame(df2)
df2['label'] = y_raw 
df2 = df2.reset_index()
df2.groupby('mv_avg300 < mv_avg120').sum()


from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_jobs=2)
clf.fit(train_X,train_y)
#clf.score(train_X,train_y) 

clf_score = clf.score(train_X, train_y)
print('RF Model Accuracy: %.2f'%clf_score)
pred_y = clf.predict(test_X)
pred_correct_ratio = 1-sum(np.abs(pred_y - test_y))/len(test_y)

print('RF Correct ratio on test data: %.2f'%pred_correct_ratio)



'''
from sklearn import svm

classifier = svm.SVC(C=2,kernel='rbf',gamma=10) # ovr:一对多策略
classifier.fit(train_X,train_y)
model_score1 = classifier.score(train_X,train_y)  

print('Correct ratio on test data: %.2f'%model_score1)
pred_y = classifier.predict(test_X)

pred_correct_ratio = 1-sum(np.abs(pred_y - test_y))/len(test_y)
print('Correct ratio on test data: %.2f'%pred_correct_ratio)

'''





