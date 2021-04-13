source ~/.bashrc
cd `dirname $0`

python run_get_kdj.py
python kdj_macd.py
python turnover_rate.py
python combine_data.py
mv ./data/hs300_tech_index.csv /home/davidyu/stock/data/shiny_data/data

mv ./data/*.csv $tmp_data_dir"/dfcf_fuquan/index_today"



