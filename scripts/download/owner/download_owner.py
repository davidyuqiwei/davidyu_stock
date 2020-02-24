from davidyu_cfg import *
from functions.connect_url import url_opener
from functions.data_dir import data_dict
from write_to_csv import *
from url_owner import *
import time
def download_owner(url1):
    ## get the table in web
    soup1 = url_opener(url1)
    t1 = soup1.find_all("table",attrs={'id':'Table1'})
    tab1 = t1[0]
    t3=tab1.find_all('tr')
    #print len(t3)
    # t4=t3[3]  ## the six one is the column names of the table
    data=[]
    for t4 in t3[3:]:
        t5=t4.find_all('td')
        cols = [ele.text.split(' ')[0] for ele in t5]
        cols[0] = cols[0].replace("\t","")
        data.append([ele for ele in cols if ele])
    return data
def save_data():
    #print data
    myfile = os.path.join(save_dir,name_in+'.csv')
    myfile_tr = os.path.join(save_dir,name_in+'_tr'+'.csv')
    write_to_csv(myfile,data)
    cmd1='iconv -f utf-8 -t GB18030 '+myfile+' >'+myfile_tr ## GB18030 the lastest coding fo chinese
    #print str(cmd1)
    os.system(cmd1)
def trans_encode(url_key,aa,string_trans_list):
    if url_key in string_trans_list:
        for k in range(0,len(aa)):
            try:
                aa[k][0] = aa[k][0].encode('latin1').decode('gbk')
                aa[k][3] = aa[k][3].encode('latin1').decode('gbk')
            except:
                pass
    else:
        pass
    return aa

def url_to_df(key_in,string_trans_list):
    url_in = url_list.get(key_in)
    aa = download_owner(url_in)
    ## if the string need trans
    aa = trans_encode(key_in,aa,string_trans_list)
    a1 = [x for x in aa if len(x)==5 and '股票简称' not in x]
    col_name = ['股票简称', '持股数量(股)', '持股比例(%)', '股本性质', '截止日期']
    df1 = pd.DataFrame(a1)
    df1.columns = col_name
    df1 = df1.sort_values('截止日期',ascending=False)
    df1.to_csv(os.path.join(save_dir,key_in+'.csv'),index=0)

if __name__ == "__main__":
    string_trans_list = ['zhongyanghuijin']
    save_dir1 = "./"
    len1 = len(owner_name)
    #key_in = 'shebao503'
    #url_in = url_list.get(key_in)
    save_dir = data_dict.get('owner')
    all_key = url_list.keys()
    print(all_key)
    input_in = sys.argv[1]
    #all_key=[input_in,'test']
    if input_in == 'all':
        for i in all_key:
            url_to_df(i,string_trans_list)
            time.sleep(3)
    else:
        print(input_in)
        url_to_df(input_in,string_trans_list)
#os.system('mv *.csv '+path_owner )

