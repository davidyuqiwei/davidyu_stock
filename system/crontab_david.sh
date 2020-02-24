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


#####################################
#           22:30 - 23:00           #
#####################################
## @description: pofa
# @run time: 50s
# @download tools: wget
# @type: daily new
##-------------pofa
############################
30 20-23 * * 1-5 MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/download/pofa/run_download_pofa.sh

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


##################### system ###########################
#######################################################
# copy import dir
45 12,23 * * * MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/copy_import_dir.sh

## kill firefox
45 12,18-22 * * * sh /home/davidyu/stock/scripts/davidyu_stock/scripts/kill_webcontent/kill_webcontent.sh

##- process all logs
57 23 * * * MakeLogFileShell.sh /home/davidyu/stock/scripts/davidyu_stock/scripts/shell_function/process_all_logs.sh
###################################################################
