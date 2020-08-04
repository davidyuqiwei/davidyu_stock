class setColname:
    def jigoudiaoyan(self):
        cols = ['ChangePercent',
         'Close',
         'CompanyCode',
         'CompanyName',
         'OrgCode',
         'OrgName',
         'OrgSum',
         'SCode',
         'SName',
         'NoticeDate',
         'StartDate',
         'EndDate',
         'Place',
         'Description',
         'Orgtype',
         'OrgtypeName',
         'Personnel',
         'Licostaff',
         'Maincontent',
         'date']
        return cols 
    def DADAN(self):
        return ["stock_index","stock_name", \
            "trade_time","price","trade_num","trade_shou", \
            "status","price_change_rate","price_change_ratio","look","date"]
    def day_history_wangyi(self):
        #日期    开盘价  最高价  最低价  收盘价  涨跌额  
        #涨跌幅(%)   成交量(手)  成交金额(万>元) >振幅(%)   换手率(%)

        return ['stock_date','open','high','low','close','change_price', \
                'change_ratio','trade_num','trade_price','variatio', \
                'turnover_rate','stock_index']       

    def dadan_sina(self):
        #   名称,代码,详情,总成交量(万股),总成交量占比,总成交额(万元),
        #   总成交额占比,平均成交价(>元),主买量(万股),中性量(万股),主卖量(万股)
        return ["stock_name","stock_index","detail","total_trade_vol", \
                "total_trade_vol_ratio","total_trade_money","total_trade_money_ratio", \
                "avg_price","zhuli_buy_vol","zhongxing_vol","zhuli_sale_vol"]
    def dadan_DFCF(self):
        return   ["new_price","today_increase_ratio","stock_index","stock_name","zhuli_liuru",
	        "chaodadan_liuru","chaodadan_liuru_ratio","dadan_liuru","dadan_liuru_ratio",
	        "zhongdan_liuru","zhongdan_liuru_ratio","xiaodan_liuru","xiaodan_liuru_ratio","test1",
	        "zhuli_liuru_ratio","test2","test3",
	        "test4","stock_date"]

