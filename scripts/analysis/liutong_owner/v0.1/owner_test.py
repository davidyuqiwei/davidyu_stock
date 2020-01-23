import pandas as pd
file1 = "/home/davidyu/stock/data/tmp/owner_list.csv"
df1 = pd.read_csv(file1)

def check_owner(x):
    #enumerate(x['owner_name_list'])
    if '香港' in x['owner_name_list'].tolist()[0]:
        x['check'] = 1
    else:
        x['check'] = 0
    return x

def test(x):
    x['tt']=1
    return x
df1.groupby('stock_index').apply(check_owner)

df1['owner_name_list']






