import os
import pandas as pd
from davidyu_cfg import *
from functions.common.getFile import *

def json_to_df(filename=None,encoding="utf8"):
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    if filename is None:
        current_dir = "./"
        return_data = get_uni_textfile(current_dir)
        filename = return_data.get('text_file_name')
        print(filename)
    f = open(filename,encoding=encoding)
    a1 = f.read()
    s1 = a1.split("}")
    strings = []
    for i in s1:
        try:
            i1 = i[2:]
            s2 = i1.split(",")
            s3 =[x.split(":")[1] for x in s2 if len(x.split(":"))>1]
            s3 = [x.replace("\"", "") for x in s3]
            strings.append(s3)
        except:
            pass
    df1 = pd.DataFrame(strings)
    return_data = {"data_out": df1,'filename': filename}
    return return_data

if __name__ == '__main__':
    return_data = json_to_df()
    print(return_data.get("data_out"))
