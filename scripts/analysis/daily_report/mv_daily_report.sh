source ~/.bashrc
cd $tmp_data_dir"/daily_report"
for i in $(ls)
do
    filedate=`echo $i | grep -Eo "[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}"`
    dirname=$stock_data"/daily_report/"$filedate
    mkdir $dirname
    mv -f $i $dirname
done

#tmp_save_dir=$tmp_data_dir"/daily_report"

#mv $tmp_save_dir/*.csv $dirname

