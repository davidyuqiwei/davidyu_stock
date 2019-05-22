## counter the list and get the most common num(1000)
# save it to csv
def list_to_csv(key_list,save_name):
    import pandas as pd
    from collections import Couter
    key_list_flat=list(iterools.chain(*key_list))
    result = Counter(key_list_flat)
    result_common = pd.DataFrame(resutl.most_common(1000))
    result_common.to_csv(save_name,index=0)
