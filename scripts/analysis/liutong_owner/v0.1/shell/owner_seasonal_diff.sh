#!/usr/bin/sh
source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
base_dir=$(dirname "$PWD")  ## the father dir of this path

database=$1
tgt_table=$2
owner_name=$3
owner_name_en=$4
start_date=$5
end_date=$6


sql_dir=$base_dir/sql
sql_file=$sql_dir/"owner_compare.sql"
echo $sql_file
spark-sql \
    -f $sql_file \
    -d database=${database} \
    -d tgt_table=${tgt_table} \
    -d owner_name=${owner_name} \
    -d owner_name_en=${owner_name_en} \
    -d start_date=${start_date} \
    -d end_date=${end_date} \
    -S

#  sh owner_seasonal_diff.sh stock_test important_owner_seasonal_change UBS ubs 2019-12-31 2020-03-31


#database="stock_test"
#tgt_table="important_owner_seasonal_change"
#owner_name="香港中央"
#owner_name_en="hk_zhongyang"
#start_date="2019-03-31"
#end_date="2019-06-30"

# ['中国工商银行股份有限公司－景顺长城沪港深精选股票型证券投资基金','香港中央结算(代理人)有限公司',
# '全国社保','国家第一养老金信托公司－自有资金','UBS']
