class html_content:
    def __init__(self):
        #self.stock_index = stock_index
        #self.year = year
        #self.date = ''
        self.html_financial_report = "http://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/%s/ctrl/%s/displaytype/4.phtml"
        self.html_pofa = "http://data.eastmoney.com/xuangu/#Yz1bY3pfaHF6YjAxXXxzPWN6X2hxemIwMXxzdD0tMQ=="
        self.html_jijin = "https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_FundStockHolder/stockid/%s.phtml"
    def html_financial_report_source(self,stock_index,year):
        year = str(year)
        return self.html_financial_report%(stock_index,year)
    #
    def html_jijin_source(self,stock_index):
        year = str(stock_index)
        return self.html_jijin%(stock_index)
'''
a1 = html_content().html_financial_report_source('000197','2018')
a2 = a1.html_financial_report_source('000197','2018')
print(a2)

'''
