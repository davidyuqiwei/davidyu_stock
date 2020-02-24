source ~/.bashrc
:<<!
this script loop the stock index to run
python file
!
#python download_jijin.py 601398
while read -r line 
do
    if [[ $line != "code" ]];then
        python download_jijin.py $line
        sleep 4.5s
    fi
done < stock_list.txt
