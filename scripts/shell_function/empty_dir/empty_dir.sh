#判断文件夹是否为空函数
is_empty_dir(){
    return `ls -A $1 | wc -w`
}

folder=$stock_data"/news_report"
outfile="empty_folder.txt"
`touch $outfile`
for file in `ls $folder`
do
    if is_empty_dir $folder"/"$file
    then
        echo $file > $outfile
    fi
done
