import os
from davidyu_cfg import *
from functions.check_data import *

owner_dict = {
    '香港中央':'hk_zhongyang',
    'UBS':'ubs',
    '全国社保':'quanguoshebao',
    '中央汇金':'zyhj',
    '中国证券金融股份有限公司':'zgzq',
    '基本养老':'jbyl'
}
if has_duplicates(owner_dict):
    raise Exception("the owner name value has duplicates")
    sys.exit(1)

database = "stock_test"
tgt_table = "important_owner_seasonal_change"
#owner_name="香港中央"
# date in '2019-03-31' '2019-06-30' '2019-09-30'
start_date = "2019-06-30"
end_date = "2019-09-30"
for i in owner_dict.keys():
    #tgt_table = owner_dict[i]
    owner_name = i
    owner_name_en = owner_dict[owner_name]
    print(tgt_table)
    print(owner_name)
    os.system("sh owner_seasonal_diff.sh %s %s %s %s %s %s" %(database,tgt_table,owner_name,owner_name_en,start_date,end_date))


#select * from stock_analysis.owner_cnt limit 10;


