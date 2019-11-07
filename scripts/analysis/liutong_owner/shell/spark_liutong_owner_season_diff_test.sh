#!/usr/bin/sh
source ~/.bashrc
cd `dirname $0`
curr_dir=`pwd`
base_dir=$(dirname "$PWD")

database="stock_test"
tgt_table=$1
owner_name=$2
start_date="2019-06-30"
end_date="2019-09-30"


sql_dir=$base_dir/sql
sql_file=$sql_dir/"run_liutong_owner_season_diff.sql"
echo $sql_file
spark-sql \
    -f $sql_file \
    -d database=${database} \
    -d tgt_table=${tgt_table} \
    -d owner_name=${owner_name} \
    -d start_date=${start_date} \
    -d end_date=${end_date} \
    -S

# ['中国工商银行股份有限公司－景顺长城沪港深精选股票型证券投资基金','香港中央结算(代理人)有限公司',
# '全国社保','国家第一养老金信托公司－自有资金','UBS']
# '香港中央结算有限公司'
