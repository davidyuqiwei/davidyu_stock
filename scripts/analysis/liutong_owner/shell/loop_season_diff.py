import os
owner_dict = {
    '香港中央结':'hk_zhongyang',
    'UBS':'ubs',
    '全国社保':'quanguoshebao'}
#print(owner_dict['a1'])
#print(owner_dict.keys())
database="stock_test"
tgt_table="important_owner_seasonal_change"
start_date="2019-03-31"
end_date="2019-06-30"

for i in owner_dict.keys():
    tgt_table = owner_dict[i]
    owner_name = i
    print(tgt_table)
    print(owner_name)
    os.system("sh spark_liutong_owner_season_diff_test.sh %s %s" %(tgt_table,owner_name))


