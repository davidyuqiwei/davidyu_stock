#source ~/.bashrc
#20 09 * * *  /home/davidyu/software/Anaconda/bin/python /download_all_news.py > /usr/davidyu/crontest.log 2>&1


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
30-59/1 9 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/DADAN/run_download_dadan_200.sh
#30-59/1 9 * * 1-5 sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/DADAN/run.sh
# 10:00 -15:00
*/1 10-11,13-15 * * 1-5 sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/DADAN/run.sh >> /usr/davidyu/crontest.log 2>&1
# data to hive
00 15 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/DADAN/DADAN_200_data_to_hive.sh


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
*/1 9-12,13-15 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/SH_index_RT/wget_SH_index_RT.sh
*/1 9-12,13-15 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/SH_index_RT/wget_SH50_index_RT.sh
*/1 9-12,13-15 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/SH_index_RT/index_amount/wget_SH_index_amount_RT.sh
#######################

## @description: download DADAN DFCF
# @run time:
# @download tools: wget
# @type: realtime
# 9:30 - 9:59

*/1 10-11,13-15 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/DFCF/dadan/run_download_dadan_DFCF.sh


#####################################
#           16:00 -   real time   #
#####################################
## @description: download DADAN > 100
# @run time: 2 hours
# @download tools: url
# @type: daily new
#---------- download DADAN off line > 100
############################################################
00 16  * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/DADAN_offline/run.sh
## data to hive

35 19 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/DADAN_offline/DADAN_offline_data_to_hive.sh


#####################################
#           17:30 - 18:00           #
#####################################
## @description: bankuai
# @run time: 20s
# @download tools: wget
# @type: daily new
## Bankuai
30 17 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/bankuai/run_download_bankuai.sh


#####################################
#           18:00 - 18:30           #
#####################################
## @description: YeJiYuQi
# @run time: 20s
# @download tools: firefox driver
# @type: daily new
00 12,18 * * * MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/YeJiYuQi/run_download_yejiyuqi.sh



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

40 20 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/dazongjiaoyi/run_download_dazongjiaoyi.sh

#####################################
#           21:00 - 21:30           #
#####################################
## @description: jigoudiaoyan
# @run time: 5s 
# @download tools: wget
# @type: daily new
##-------jigoudiaoyan
40 21 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/JiGouDiaoYan/run_download_jigoudiaoyan.sh

#####################################
#           22:30 - 23:00           #
#####################################
## @description: pofa DFCF
# @run time: 50s 
# @download tools: wget
# @type: daily new
##-------------pofa
############################
30 20-23 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/pofa/run_download_pofa.sh

## @description: import owner DFCF
# @run time: 50s
# @download tools: wget
# @type: daily new
##-------------important owner
############################
35 21 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/important_owner/run_download_important_owner.sh



## @description: gainian  liuru
# @run time: 50s
# @download tools: wget
# @type: daily new
##----------- gainian liuru
############################
55 21 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/gainian_liuru/run_download_gainian_liuru.sh

########################################
#               weekly                 #
########################################
# @description: download daily historical stock data
# @run time :
# @download tools: url
# @type: all

30 7 * * 6 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/online/download/day_history/run.sh

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
45 12,18-22 * * * sh /home/davidyu/stock/scripts/davidyu_stock/scripts/kill_webcontent/kill_webcontent.sh

##- process all logs
57 23 * * * MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/shell_function/process_all_logs.sh
###################################################################
