def generate_stock_index(i):
    '''
    input : i stock index raw input  '601398'/  '917'
    output : 601398.ss
            000917.sz
    '''
    if len(str(i))<6:
        stock_index = str(i).zfill(6)+'.sz'
    elif str(i)[0] == '6':  ## download for ShangHai
        stock_index = str(i)+'.ss'
    elif str(i)[0] == '0':
        stock_index = str(i)+'.sz'
    return stock_index

def stk_index_list_gen():
    ''' 
    functions : get the stock index list without "3XXXXX" chuangyeban 
    output:  list
            list of all stock index
    '''
    from dir_control.data_dir_v1 import stk_index_list
    ## remove '300'
    stk_index_list=[x for x in stk_index_list if str(x).zfill(6)[0]!='3']
    return stk_index_list
