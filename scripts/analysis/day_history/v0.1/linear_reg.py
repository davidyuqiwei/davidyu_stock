from davidyu_cfg import *
from get_data import *
from functions.DF_process import *


def linear_REG(x):
    print(x.head(3))
    #reg1 = LinearReg()
    x['norm_adj_close'] = norm_col(x,"adj_close")
    try:
        x1 = x.drop_duplicates().sort_values('stock_date')
        slope, inter = reg1.single_linear_reg(x1,"norm_adj_close")
        row_len = x.shape[0]
    except:
        slope = -999
        row_len = 0
    return slope,row_len


#a1=df1.iloc[0:100,:].groupby('stock_index').apply(linear_REG)

df1 = pd.read_csv("test_data.csv")

data_vv = df1.groupby('stock_index')
stock_ind = []
stock_slope = []
stock_row_len = []
for name,group in data_vv:
    slope,row_len = linear_REG(group)
    stock_ind.append(name)
    stock_slope.append(slope)
    stock_row_len.append(row_len)
    #print(slope)

data_dict = {
        'stock_index': stock_ind,
        'slope': stock_slope,
        'row_len': stock_row_len
        }
df_out = pd.DataFrame(data_dict)
print(df_out.sort_values('slope',ascending=False))
df_out.to_csv("slope.csv",index=0)
#print(a1)
#slope, inter = t1.single_linear_reg(df1,"adj_close")


