from download_liutong_owner import *
from download_liutong_owner import _transform_data
stock_index='603383'
html1='http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CirculateStockHolder/stockid/%s/displaytype/3000.phtml' %stock_index
#data1=down(html1)
#data1['stock_index']=stock_index
#data_raw=data1.copy(deep=True)
#data2=_transform_data(data1)
process(stock_index,"./")
