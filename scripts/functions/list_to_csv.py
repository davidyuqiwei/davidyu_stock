## counter the list and get the most common num(1000)
# save it to csv
def list_to_csv(key_list,save_name):
    """
    key_list: the list of list -- of string
    make it flat and count of each value and save to dataframe
    """
    import pandas as pd
    from collections import Counter
    import itertools
    key_list_flat=list(itertools.chain(*key_list))
    result = Counter(key_list_flat)
    result_common = pd.DataFrame(result.most_common(1000))
    result_common.to_csv(save_name,index=0)
