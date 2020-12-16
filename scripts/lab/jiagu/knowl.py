import jiagu
from davidyu_cfg import *
from functions.data_dir import *
from functions.get_datetime import *

data_dir = "/home/davidyu/stock/data/news_report/601398"


def get_knowledge(file_in):
    f = open(file_in,encoding=encode_in)
    content = f.read()
    kl = jiagu.knowledge(content)
    return kl

encode_in = "utf-8"
files = os.listdir(data_dir)
kl_in = []
for i in files:
    file_in = os.path.join(data_dir,i)
    out = get_knowledge(file_in)
    if len(out) > 0:
        kl_in.append(out)



