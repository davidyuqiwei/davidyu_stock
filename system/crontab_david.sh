#source ~/.bashrc
#20 09 * * *  /home/davidyu/software/Anaconda/bin/python /download_all_news.py > /usr/davidyu/crontest.log 2>&1

#####################################
#           16:00 -   real time   #
#####################################

# @description:     download DADAN > 100
# @run time:        2 hours
# @download tools:  url - python
# @type:            daily new
# @source:          ifeng, 
#---------- download DADAN off line > 100
############################################################

32 15  * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/dadan_real_time_ifeng/run_main_dadan_real_time_ifeng.sh

# dfcf_fuquan
23 15 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/dfcf_fuquan/run_main_dfcf_fuquan.sh

## dfcf all owner update
00 23 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/all_owner/run_main_all_owner.sh

## trade dates
00 20 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/clean_data/run_stock_dw.sh


20 03 * * 1-6 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/dfcf_fuquan/modelling/v1/run_all.sh

#####################################
#           1:00-3:30               #
#####################################

# @description:   download zhulikongpan data
# @run time :about 6 hours
# @download tool:  wget
# @type: daily new
# @source: DFCF,   http://data.eastmoney.com/stockcomment/002594.html

56 19 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/fenhong/run_main_fenhong.sh

10 06 * * 1-7 MakeLogFileShell.sh /home/davidyu/stock/data/shiny_data/app/restart_app.sh

30 06 * * 1-7 MakeLogFileShell.sh /home/davidyu/stock/data/shiny_data/python/zhulikongpan/run_shiny_zhulikongpan.sh

10 22 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/dfcf_longhubang/run_main_dfcf_longhubang.sh

42 23 * * 1-6 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/zhulikongpan/run_main_zhulikongpan.sh
#stock shizhi
10 08 * * 6 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/stock_shizhi/run_main_stock_shizhi.sh
# dfcf_bankuai_zijin
15 20 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/dfcf_bankuai_zijin/run_main_dfcf_bankuai_zijin.sh
# dfcf bankuai diyu,hangye
20 20 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/dfcf_bankuai/run_main_dfcf_bankuai.sh

# hk stock owner
30 04 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/hk_stock_owner/run_main_hk_stock_owner.sh

# dadan realtime 1000
45 19 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/dadan_real_time_ifeng_1000/run_main_dadan_real_time_ifeng_1000.sh

# dfcf hugutong 
22 03 * * 1-6 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/dfcf_hugutong/run_main_dfcf_hugutong.sh


# @description:   download baostock data
# @run time :about >5 hours
# @download tool:  python api
# @type: daily new
# @source: DFCF, baostock
#10 23 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/baostock/run_main_baostock.sh

# @description:   download volume price distribution of every stock
# @run time :about 6 hours
# @download tool:  url
# @type: daily new
# @source: sina,   https://vip.stock.finance.sina.com.cn/quotes_service/view/cn_price.php?symbol=sh601398
53 18 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/volume_price_distr/run_main_volume_price_distr.sh

#####################################
#           6:00-6:30               #
#####################################

#####################################
#           7:00-7:30               #
#####################################

# @description: download outside news website: sina,ifeng   !! 
# @run time :about 5 minutes
# @download tool firefox driver
# @type: daily new
30 7 * * * MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/online/download/all_news/run_download_all_new.sh 


#####################################
#           8:00-8:30               #
#####################################
# @description:download shenzhen shanghai index
# @run time:
# @download tools: R
# @type:all data
00 8 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/online/download/SH_SZ_index/run_download_SH_SZ_index.sh


#####################################
#           9:00-15:30  real time   #
#####################################
## @description: download DADAN > 200, realtime
# @run time:
# @download tools: url
# @type: realtime
# 9:30 - 9:59

#30-59/1 9 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/DADAN/run_download_dadan_200.sh
#30-59/1 9 * * 1-5 sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/DADAN/run.sh
# 10:00 -15:00
#*/1 10-11,13-15 * * 1-5 sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/DADAN/run.sh >> /usr/davidyu/crontest.log 2>&1
# data to hive
#00 15 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/DADAN/DADAN_200_data_to_hive.sh

## ----- test for sina
#*/1 10-11,13-15 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/dadan_sina/run_download_dadan_sina_realtime.sh

##==== sina dadan offline
#40 15 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/dadan_sina_offline/run_main_dadan_sina_offline.sh

## @description: fushi A50
# @run time:
# @download tools: wget
# @type: realtime
# 9-12 13-23,0-6

*/1 * * * * sleep 38;MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/fushi_a50/wget_fushi_a50.sh


## @description: oumei future index, nsdaq index
# @run time:
# @download tools: wget
# @type: realtime
# 9-12 13-23,0-6
*/1 * * * * sleep 18;MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/oumei_future_index/run_download_oumei_future_index.sh

*/1 * * * * sleep 28;MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/nsdaq/run_download_nsdaq_RT.sh

#*/1 9-12 * * * MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/fushi_a50/wget_fushi_a50.sh

## @description: SH index realtime
# @run time:
# @download tools: wget
# @type: realtime
# 9-12 13-23,0-6
#*/1 9-12,13-15 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/SH_index_RT/wget_SH_index_RT.sh
*/1 9-12,13-15 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/SH_index_RT/wget_SH50_index_RT.sh
*/1 9-12,13-15 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/SH_index_RT/index_amount/wget_SH_index_amount_RT.sh
#######################

## @description: download DADAN DFCF
# @run time:
# @download tools: wget
# @type: realtime
# 17:35-17:40

38 17 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/dadan_DFCF/run_main_dadan_DFCF.sh


## data to hive

#35 19 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/DADAN_offline/DADAN_offline_data_to_hive.sh


#####################################
#           16:00 -   real time   #
#####################################
## @description: download wangyidata
# @run time: 2.5 hours
# @download tools: url
# @type: daily new
############################################################
32 03 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/day_history_wangyi/run_main_day_history_wangyi.sh

#####################################
#           17:30 - 18:00           #
#####################################
## @description: bankuai
# @run time: 20s
# @download tools: wget
# @type: daily new
## Bankuai
30 17 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/bankuai/run_main_bankuai.sh


#####################################
#           18:00 - 18:30           #
#####################################
## @description: YeJiYuQi
# @run time: 20s
# @download tools: firefox driver
# @type: daily new
00 21,22,23 * * * MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/YeJiYuQi/run_main_YeJiYuQi.sh



#####################################
#           20:00 - 20:30           #
#####################################

## @description: future_index
# @run time: check
# @download tools: firefox driver
# @type: daily new
30 18-20  * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/future_index/run_download_index_future.sh

## @description: dazongjiaoyi
# @run time: 20s
# @download tools: wget 
# @type: daily new

40 19 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/dazongjiaoyi/run_main_dazongjiaoyi.sh

#####################################
#           21:00 - 21:30           #
#####################################
## @description: jigoudiaoyan
# @run time: 5s 
# @download tools: wget
# @type: daily new
##-------jigoudiaoyan
00 21 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/JiGouDiaoYan/run_main_JiGouDiaoYan.sh

#####################################
#           22:30 - 23:00           #
#####################################
## @description: pofa DFCF
# @run time: 50s 
# @download tools: wget
# @type: daily new
##-------------pofa
############################
30 22 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/pofa/run_download_pofa.sh

## @description: import owner DFCF
# @run time: 50s
# @download tools: wget
# @type: daily new
##-------------important owner
############################
35 21 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/important_owner/run_main_important_owner.sh



## @description: gainian  liuru
# @run time: 50s
# @download tools: wget
# @type: daily new
##----------- gainian liuru
############################
55 21 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/gainian_liuru/run_download_gainian_liuru.sh

## @description: gainian,bankuai sina
# @run time: 50s
# @download tools: wget
# @type: daily new
##----------- gainian liuru
############################
55 20 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/bankuai_sina/run_main_bankuai_sina.sh

########################################
#               weekly                 #
########################################
# @description: download daily historical stock data
# @run time :
# @download tools: url
# @type: all

#30 7 * * 6 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/online/download/day_history/run.sh

# @description: download xiaopangu 小盘股 from dongfangcaifu
# @run time : 10s
# @download tools: wget
# @type: all
30 6 * * 6 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/DFCF/xiaopangu/run_download_xiaopangu.sh


## daily report
# @description: make daily report for davidyu
# @run time : 30s
# @tools: python
# @type: all
38 23 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/daily_report/run_daily_report.sh


##################### system ###########################
#######################################################
# copy import dir
45 12,23 * * * MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/copy_import_dir.sh

## kill firefox
45 10,11,17,23 * * * sh /home/davidyu/stock/scripts/davidyu_stock/scripts/kill_webcontent/kill_webcontent.sh

##- process all logs
57 23 * * * MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/shell_function/process_all_logs.sh
###################################################################
## combine log
* * * * * /usr/bin/sh /home/davidyu/stock/scripts/davidyu_stock/scripts/analysis/checkData/combine_log/combineLog.sh
