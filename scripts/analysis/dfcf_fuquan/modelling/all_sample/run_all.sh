source ~/.bashrc
cd `dirname $0`

sh /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/feature_center/rolling_regression/run_3.sh >/dev/null 
sh /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/feature_center/rolling_regression/run_5.sh >/dev/null 

sh /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/feature_center/kdj_macd/stock_index/run_macd.sh > /dev/null

sh /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/feature_center/combine_data/stock_index/run_combine_macd_rollregression.sh 3 > /dev/null 
sh /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/feature_center/combine_data/stock_index/run_combine_macd_rollregression.sh 5 > /dev/null 

sh run_xgb_model.sh > a.log 2>&1 

sh run_xgb_predict.sh

python process_predict.py















