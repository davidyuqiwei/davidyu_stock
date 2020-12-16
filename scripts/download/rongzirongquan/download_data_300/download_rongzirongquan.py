import sys
from davidyu_cfg import *
from functions.connect_url import url_opener
from functions.data_dir import *
from functions.get_datetime import *
from functions.common.save_DataFrame import save_df_date
from functions.common.TimeMake import *
import re

html1 = "http://datacenter.eastmoney.com/api/data/get?callback=datatable3319302&type=RPTA_WEB_RZRQ_GGMX&sty=ALL&source=WEB&p=2&ps=5000&st=RZJME&sr=-1&filter=(date%3D%272020-11-26%27)&pageNo=1&_=1607562655494"

def get_page_num(html1):
    soup2 = url_opener(html1)
    a1=soup2.get_text()
    reg = r'pages(.{3})' ## find 3 str after page
    wordreg = re.compile(reg)
    a2 = re.findall(wordreg,a1)
    page_num = a2[0][2]
    return page_num

def get_html(page):
    html1 = "http://datacenter.eastmoney.com/api/data/get?callback=datatable2031983&type=RPTA_RZRQ_LSHJ&sty=ALL&source=WEB&st=dim_date&sr=-1&p="+page+"&ps=500&filter=&pageNo=1&_=1607570467755"
    return html1

for p1 in range(1,7):
    try:
        os.system("sh run_download_rongzirongquan.sh %s "%(str(p1)))
        time.sleep(2)
    except Exception as e:
        logging.error(e)
        pass
