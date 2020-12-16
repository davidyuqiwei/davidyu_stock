import os

owner_dict = {
    '香港中央':'hk_zhongyang',
    'UBS':'ubs',
    '全国社保':'quanguoshebao',
    '中央汇金':'zyhj'
    }

database="stock_test"
tgt_table="important_owner_seasonal_change"
#owner_name="香港中央"
start_date = "2020-03-31"
end_date = "2020-06-30"
for i in owner_dict.keys():
    #tgt_table = owner_dict[i]
    owner_name = i
    owner_name_en = owner_dict[owner_name]
    print(tgt_table)
    print(owner_name)
    os.system("sh owner_seasonal_diff.sh %s %s %s %s %s %s" %(database,tgt_table,owner_name,owner_name_en,start_date,end_date))


#select * from stock_analysis.owner_cnt limit 10;


