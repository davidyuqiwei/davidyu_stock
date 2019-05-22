def find_market(stk):
    if stk.startswith('00'):
        market='shenzhen'
    elif stk.startswith('60'):
        market='shanghai'
    else:
        print('wrong input stock number')
find_market('601398')
