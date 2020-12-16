import pandas as pd
from davidyu_cfg import *
from functions.rolling_regression import *
from functions.day_history.rollReg import rollRegDayHis
#from functions.models.davidCluster import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist,tmp_data_dict
from sklearn.model_selection import train_test_split
from functions.models.cnn import *
save_dir = tmp_data_dict.get("SH_index")
df3 = pd.read_csv(os.path.join(save_dir,"model_data.csv"))
feature_list = np.load("all_feature.npy").tolist()

Y = df3.slopes.values
X = df3[feature_list].values

#Y = np.array([0 if x <0 else 1 for x in Y])
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.3)

x_train = np.expand_dims(x_train,axis=-1)
y_train = np.expand_dims(y_train,axis=-1)
n_timesteps, n_features, n_outputs =x_train.shape[0], x_train.shape[1], y_train.shape[1]

#model = CNN_model(x_train,y_train,n_features,x_test,y_test)
model = CNN_model(x_train,y_train)

x_test1 = np.expand_dims(x_test,axis=-1)
y_predict = model.predict_classes(x_test1)

y_predict = list(map(str, y_predict))
y_predict = [int(x) for x in y_predict]
print('准确率', metrics.accuracy_score(y_test, y_predict))
print('平均f1-score:', metrics.f1_score(y_test, y_predict, average='weighted'))


