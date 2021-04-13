source ~/.bashrc
cd `dirname $0`
sh run_dadan_dfcf.sh
sh run_dazongjiaoyi.sh
sh run_important_owner.sh
sh run_jigoudiaoyan.sh
sh run_dfcf_bankuai.sh
sh run_dadan_realtime.sh
python split_dadan_realtime.py

sh ../python/macd/run_macd.sh
python ../python/dadan_dfcf/split_dadan_dfcf.py
sh ../python/zhulikongpan/run_shiny_zhulikongpan.sh


#python split_dadan_realtime.py

sh copy_data.sh


Rscript --slave --no-save --no-restore trans_dadan_data.r
