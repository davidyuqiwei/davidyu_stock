from davidyu_cfg import *
from functions.connect_url import url_opener
import os

h1 = url_opener("http://snap.stanford.edu/class/cs224w-2012/handouts.html")

a1 = h1.findAll('a') 
for a2 in a1:
    a3 = a2.get('href')
    if '.pdf' in a3:
        os.system('wget '+a3)




