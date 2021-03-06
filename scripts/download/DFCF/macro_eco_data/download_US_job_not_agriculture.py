import sys
from davidyu_cfg import *
from functions.connect_url import url_opener
import time

html1 = "http://data.eastmoney.com/cjsj/goldforexreserve.aspx?p=%s"

def url_to_df(html1):
    soup2 = url_opener(html1)
    a2 = soup2.find_all('table')
    a3 = a2[0].find_all('tr')
    data_list_all = []
    for i in range(2,len(a3)):
        a5 = a3[i].get_text()
        data_list = [x.strip() for x in a5.split("\r\n")]
        data_list = [x for x in data_list if x != '']
        data_list_all.append(data_list)
    df1 = pd.DataFrame(data_list_all)
    df1.dropna(axis=0, how='any', inplace=True)
    return df1
if __name__ == "__main__":
    html1 = "http://data.eastmoney.com/cjsj/foreign_0_2_%s.html"
    #df1 = url_to_df(html1)
    #print(df1)
    df2 = pd.DataFrame()
    for i in range(1,8):
        url_in = html1 %(str(i))
        df1 = url_to_df(url_in)
        df2 = df2.append(df1)
        time.sleep(2.3)
    cols = ["date","before_value","now_value","report_date"]
    df2.columns = cols
    df2.to_csv("US_job_not_agriculture.csv",index=0)

