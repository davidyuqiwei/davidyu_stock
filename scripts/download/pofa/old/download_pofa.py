from davidyu_cfg import *
from functions.connect_url import driver_open_noBS
from functions.connect_url import *
from bs4 import BeautifulSoup as BS
from functions.get_datetime import *
from functions.data_dir import *
from functions.html_list import html_content

#html  = "http://data.eastmoney.com/xuangu/#Yz1bY3pfaHF6YjAxXXxzPWN6X2hxemIwMXxzdD0tMQ=="


def process_html():
    from functions.html_list import html_content
    hh = html_content()
    html = hh.html_pofa  ## read the html
    html_content = driver_open_noBS(html)
    soup1 = BS(html_content.encode("gbk"))
    stock_name1 = soup1.find_all("td",attrs={'class','name'}) ## stock name
    stock_index_raw = soup1.find_all('a',target="_blank") 
    return stock_name1,stock_index_raw

def get_stock_index_name(stock_name1,stock_index_raw):
    stock_index = []
    for i in stock_index_raw:
        stock_index_string = i.get_text()
        if stock_index_string.startswith('6') or stock_index_string.startswith('3') or stock_index_string.startswith('0'):
            stock_index.append(stock_index_string)
    stock_name = []
    for j in stock_name1:
        stock_name2 = j.get_text().strip()
        stock_name.append(stock_name2)
    return stock_index,stock_name

def content_to_DF(stock_index,stock_name):
    df1 = pd.DataFrame(columns=['stock_index','stock_name','stock_date','day'])
    now_date,now_date_time = get_the_datetime()
    df1['stock_index'] = stock_index
    df1['stock_name'] = stock_name
    df1['stock_date'] = now_date
    df1['day'] = now_date
    return df1,now_date
def save_data(DF,now_date):
    save_dir = data_dict.get("pofa")
    save_file = now_date+".csv"
    DF.to_csv(os.path.join(save_dir,save_file),index=0)

def main():
    print("start")
    stock_name1,stock_index_raw = process_html()
    print("process html")
    stock_index,stock_name = get_stock_index_name(stock_name1,stock_index_raw)
    print("get stock index and name")
    df1,now_date = content_to_DF(stock_index,stock_name)
    save_data(df1,now_date)

if __name__ =='__main__':
    main()
