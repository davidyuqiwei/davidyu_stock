from load_model_data import *
import numpy as np

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

df1 = load_data()
#y_raw = [1 if x>0 else 0 for x in df1.adj_close.diff().tolist() ]

start_index = 1980

#df1.drop(df1.columns[[0,1,2]], axis=1, inplace=True)
df1 = df1[start_index:]
feature_col = ['index','mv_avg5', 'mv_avg10', 'mv_avg15',
               'mv_avg20', 'mv_avg30', 'mv_avg40', 'mv_avg50', 'mv_avg60', 'mv_avg120',
                'mv_avg150', 'mv_avg200', 'mv_avg300']

close


df_fea = df1[feature_col]
#y_raw = [1 if x>0 else 0 for x in df1.adj_close.diff().tolist() ]

df1 = df1.sample(frac=1)
y_raw = [1 if x>0 else 0 for x in df1.adj_close.diff().tolist() ]
#df1.drop(df1.columns[[0,1,2]],axis=1, inplace=True)
df1.drop(df1.columns[[1,2]],axis=1, inplace=True)

df1 = df1[df1.columns[[0,3,4,5,6]]]
import featuretools as ft
#df1 ['id'] = df1['close7'] + df1 ['close8']
es = ft.EntitySet(id = 'sales')
es.entity_from_dataframe(entity_id = 'bigmart', dataframe = df_fea, index = 'index')
#es.normalize_entity(base_entity_id ='bigmart',new_entity_id ='outlet',index ='mv_avg5',additional_variables = feature_col)


#primitives[primitives['type'] == 'transform'].head(100)
#primitives[primitives['type'] == 'aggregation'].head(10)


feature_matrix,feature_names = ft.dfs(entityset = es,
target_entity ='bigmart',
max_depth = 3,
agg_primitives=['mean','max','std'],
trans_primitives = ['less_than'],
verbose = 1,
n_jobs = 2)



x_raw = normalize_DF(df1)
y_raw = np.array(y_raw)
data_len = x_raw.shape[0]

train_index = int(data_len*0.7)
test_index = train_index + int(data_len*0.2)
predict_index = data_len


x_input1 = x_raw.values[start_index:train_index]
y_input1 = y_raw[start_index:train_index]

train_X = x_input1
train_y = y_input1

test_X = x_raw.values[train_index:test_index]
test_y = y_raw[train_index:test_index]

from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(max_depth=15,min_samples_split=2,random_state=0)

tree.fit(train_X, train_y)
model_score = tree.score(train_X, train_y)
print('DT Model Accuracy: %.2f'%model_score)


pred_y = tree.predict(test_X)

pred_correct_ratio = 1-sum(np.abs(pred_y - test_y))/len(test_y)
print('DT Correct ratio on test data: %.2f'%pred_correct_ratio)

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





