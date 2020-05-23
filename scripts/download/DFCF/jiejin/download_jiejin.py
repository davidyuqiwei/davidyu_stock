import json
import pandas as pd
from davidyu_cfg import *
from functions.data_dir import *



def jsonStrClean(x):
    x = x.replace("},","}").replace('{','').replace(']','').replace('}','')
    x1 = '{'+x+'}'
    return x1
def makeJiejinDF(jsonStrs):
    data_json_list = []
    font_code_list = []
    for jsonStr in jsonStrs:
        try:
            a4 = jsonStrClean(jsonStr)
            a5 = json.loads(a4)
            if len(a5) == 17:
                data_json_list.append(a5)
            if len(a5) == 2:
                font_code_list.append(a5)
        except:
            pass
    jiejin_df = pd.DataFrame(data_json_list)
    font_df = pd.DataFrame(font_code_list)
    #a_dict = font_df.to_dict()
    font_df_dict = {key:value for key, value in  font_df.values}
    return jiejin_df,font_df_dict
def replaceFontCode(x,font_df_dict):
    '''
    relace the number code from DFCF
    '''
    try:
        for key1 in font_df_dict.keys():
            x = x.replace(key1,str(font_df_dict.get(key1)))
    except:
        pass
    return x

if __name__=='__main__':
    data_in = open('test.txt',encoding='utf-8')
    data_json = data_in.read()
    data_split = data_json.split("{")
    jiejin_df,font_df_dict = makeJiejinDF(data_split)
    jiejin_df1 = jiejin_df.applymap(lambda x:replaceFontCode(x,font_df_dict))  
    data_dir = data_dict.get("jiejin")
    jiejin_df1.round(3).to_csv(os.path.join(data_dir,"jiejin_history.csv"),index=0)
    print(jiejin_df1.head(10))





