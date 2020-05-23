import json
import pandas as pd
a1=open('test.txt',encoding='utf-8')
a2=a1.read()
a3 = a2.split("{")
data_json_list = []
font_code_list = []

def jsonStrClean(x):
    x = x.replace("},","}").replace('{','').replace(']','').replace('}','')
    return x
for jsonStr in a3:
    try:
        a4 ='{'+jsonStrClean(jsonStr)+'}'
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




def replaceFontCode(x):
    try:
        for key1 in font_df_dict.keys():
            x = x.replace(key1,str(font_df_dict.get(key1)))
    except:
        pass
    return x

jiejin_df1 = jiejin_df.applymap(lambda x:replaceFontCode(x))  
print(jiejin_df1.head(10))
