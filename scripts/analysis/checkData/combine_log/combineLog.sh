#!/usr/bin/sh
source ~/.bashrc
#cd $log_dir
cd `dirname $0`
while read -r line 
do  
    save_log=$log_dir"/""all_"$line".log"
    touch $save_log
    cat $log_dir"/"$line* >> $save_log
    rm -rf $log_dir"/"$line*
done < log_list.txt



#cat wget_SH_index_RT * > all_wget_SH_index_RT.log
#rm -rf  wget_SH_index_RT*

#cat wget_SH_index_amount_RT * > all_wget_SH_index_amount_RT.log
#rm -rf wget_SH_index_amount_RT*


