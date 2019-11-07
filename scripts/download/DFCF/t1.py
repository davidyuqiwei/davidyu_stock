from davidyu_cfg import *
from functions.connect_url import driver_open_noBS
from functions.connect_url import *
from bs4 import BeautifulSoup as BS

html = driver_open_noBS("http://data.eastmoney.com/gdfx/ShareHolderDetail.aspx?hdCode=80637337&hdName=%CF%E3%B8%DB%D6%D0%D1%EB%BD%E1%CB%E3%D3%D0%CF%DE%B9%AB%CB%BE")
a1 = driver_open_noBS(html)  
