## save the raw history data adj_close
#selectHistoryPartData.py
python saveRollRegression.py
#spark-submit saveDaZongJiaoYiFeature.py
python saveMvAvgFeature.py
python saveHistoryFeature.py

python combineData.py
python modelling.py
python predict.py


