# from framework.davidyu_cfg import *
# from common.py.parse_to_df import *
# from common.py.base_parameter import BaseParameter
# from common.py.parse_to_df_all_owner import *
# from functions.get_datetime import *
# from common.py.time_make import *
# from common.py.clean_data import *
# from functions.common.dfProcess import dfProcess
# from functions.data_dir import create_dir_if_not_exist
# from functions.update.cleanData import cleanData

from pandas.io.json import json_normalize
import re
import json
import pandas as pd


def make_it_json(input_str):
    if input_str[0] != "{":
        input_str = "{" + input_str
    if input_str[-1] != "}":
        input_str = input_str + "}"
    return input_str


def parse_to_df(input_str):
    get_data = re.findall(r'[[](.*?)[]]', input_str)[0]
    get_data_split = get_data.split('},{')
    df_list = []
    for x in get_data_split:
        aa3 = make_it_json(x)
        aa2 = json.loads(aa3)
        df1 = json_normalize(aa2)
        df_list.append(df1)
    df_out = pd.concat(df_list)
    print(df_out)
    return df1



if __name__ == "__main__":
    file_in = "test.txt"
    with open(file_in) as f: ss = f.read()
    print(ss)
    parse_to_df(ss)
    # df1 = parse_data_to_df(file_in)
    # save_data(df1)
    # save_to_shiny(df1)
