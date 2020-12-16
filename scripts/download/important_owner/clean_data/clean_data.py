from davidyu_cfg import *
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
from functions.get_datetime import *
data_file = os.path.join(tmp_data_dict.get("important_owner"),"important_owner.csv")


now_date = get_the_datetime()[0]


f = open(data_file, 'r')
data1 = f.read()

data2 = data1.split("\n")
data_in = []
for i in data2:
    if len(i)>0:
        i1 = i.split(",")
        if i1[17] != "17":
            data_in.append(i.split(",")[0:18])

cols = ["id","id2","owner_name","owner_type","stock_type","gudong_rank",
            "stock_index","stock_name","change_date","num","chigu_ratio",
            "liutong_ratio","report_date","change_type",
            "change_ratio","test1","test2","num_change"
      ]

df1 = pd.DataFrame(data_in)
df1.columns = cols
df1["stock_date"] = now_date
df1.to_csv(data_file,index=0)

f.close()



