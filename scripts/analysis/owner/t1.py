from davidyu_cfg import *
from functions.connect_url import url_opener
from functions.data_dir import data_dict

data_dir = data_dict.get("owner")
#df1 = pd.read_csv(os.path.join(data_dir,"zhongyanghuijin.csv"))
df1 = pd.read_csv(os.path.join(data_dir,"hk_central.csv"))

#df1.groupby("股票简称")



def latest_change(x):
    date_in = x["截止日期"].tolist()[0]
    change1 = x["持股比例(%)"].diff(-1).reset_index()['持股比例(%)'].tolist()[0]
    change = round(change1,2)
    df2 = pd.DataFrame(columns=["date_latest","latest_change"])
    df2['date_latest'] = [date_in]
    df2["latest_change"] = [change]
    return df2

aa = df1.groupby("股票简称").apply(latest_change)

a1 = aa.dropna().sort_values("latest_change")
a2 = a1[a1["date_latest"]>"2019-09-01"]
print(a2.tail(30))

'''
a1.sort_values("date_latest")
df2 = df1[df1["股票简称"]=="华峰氨纶"]

df2["持股比例(%)"].diff(-1)
df2["持股比例(%)"].diff(-1)[0]

'''



