download_txt="bankuai_"$(date "+%Y%m%d")".txt"
wget http://money.finance.sina.com.cn/q/view/newFLJK.php?param=class -O $download_txt
sed -i 's/var S_Finance_bankuai_class = //g' $download_txt
python download_bankuai.py $download_txt
