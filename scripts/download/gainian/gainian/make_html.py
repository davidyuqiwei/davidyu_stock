#base_url = "http://xuanguapi.eastmoney.com/Stock/JS.aspx?type=xgq&sty=xgq&token=eastmoney&c=[gfzs8(BK%s)]" ## area
base_url = "http://xuanguapi.eastmoney.com/Stock/JS.aspx?type=xgq&sty=xgq&token=eastmoney&c=[gfzs7(BK%s)]" # gainian
#base_url = "http://xuanguapi.eastmoney.com/Stock/JS.aspx?type=xgq&sty=xgq&token=eastmoney&c=[gfzs6(BK%s)]"

for i in range(500,1000):
    str_in = str(i).zfill(4)
    html1 = base_url%(str_in)
    print(html1)


