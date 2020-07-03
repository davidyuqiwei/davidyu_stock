import pandas as pd

file1 = "/home/davidyu/stock/data/test/fin_report_index_cnt.csv"
df1 = pd.read_csv(file1)
df1.columns = [x.split(".")[1] for x in df1.columns.tolist()]
df2 = df1.T.reset_index()
df2.columns = ["index","cnt"]


high_index = df2[df2["cnt"]>50]
index_out = [x.split("_")[0] for x in high_index["index"].tolist() ]
# copy to getFinReportFeature
print(",".join(index_out))

