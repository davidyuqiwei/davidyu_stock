from davidyu_cfg import *
from functions.connect_url import url_opener
from bs4 import BeautifulSoup as BS


f = open("url1.txt")

str1 = f.read()
str2 = BS(str1,"html.parser")

a1 = str2.find_all("tr")
strs = []
for i in a1[1:]:
    all_text = i.get_text()
    all_text_clean = [x for x in all_text.split(" ") if len(x)>0]
    strs.append(all_text_clean)
df1 = pd.DataFrame(strs) 




