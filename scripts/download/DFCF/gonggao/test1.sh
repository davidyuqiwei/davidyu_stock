file1="jijin_hetong.txt"
wget "http://xuanguapi.eastmoney.com/Stock/JS.aspx?type=xgq&sty=xgq&token=eastmoney&c=[cz_jgcg02][cz_ggxg07]&p=1&jn=KFuFnMSA&ps=1000&s=cz_ggxg07&st=" -O $file1

sed -i 's/var KFuFnMSA=//g' $file1
