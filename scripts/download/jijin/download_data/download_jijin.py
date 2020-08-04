from davidyu_cfg import *
from functions.connect_url import url_opener
from functions.data_dir import data_dict,stk_index_list,create_dir_if_not_exist
import re
zhmodel = re.compile(u'[\u4e00-\u9fa5]')

def process_html(stock_index):
    from functions.html_list import html_content
    html = html_content().html_jijin_source(stock_index)
    soup2 = url_opener(html)
    table1 = soup2.find_all(id="FundHoldSharesTable")
    table2 = table1[0]
    rows = table2.find_all('tr')
    return rows

def make_df():
    df1 = pd.DataFrame(columns=['基金名称', '基金代码', '持仓数量', '占流通股比例', '持股市值', '占净值比例','stock_date'])
    return df1

def content_to_df(rows,df1):
    try:
        for i in rows[1:]:
            str1 = i.get_text()
            match = zhmodel.search(str1)
            strings_in = str1.split("\n")
            if match:
                pass
            else:
                strings_in = str1.encode("latin1").decode("gbk").split("\n")
            if '截止日期' in strings_in:
                date = strings_in[2]
                #print(date)
            elif '基金名称' in strings_in:
                pass
            elif '基金名称' not in strings_in and len(strings_in)==8:
                df_in = pd.DataFrame(strings_in[1:7]+[date]).T
                df_in.columns = ['基金名称', '基金代码', '持仓数量',\
                        '占流通股比例', '持股市值', '占净值比例','stock_date']
                df1 = pd.concat([df1,df_in])
    except:
        print("failed stock_index  "+ stock_index)
        pass
    return df1
def save_data(df,stock_index):
    save_dir = data_dict.get("jijin")
    save_file = os.path.join(save_dir,stock_index+".csv")
    df.to_csv(save_file,index=0)
def main(stock_index):
    rows = process_html(stock_index)
    df1 = make_df()
    df_out = content_to_df(rows,df1)
    df_out['stock_index'] = stock_index
    save_data(df_out,stock_index)
    #print(df_out.head())
    #print(df_out.tail())

if __name__ =='__main__':
    stock_index = sys.argv[1]
    main(stock_index)
#rows[3].get_text()


