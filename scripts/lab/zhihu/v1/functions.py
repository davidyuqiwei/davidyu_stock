from selenium import webdriver
from bs4 import BeautifulSoup as BS
import os
#import urllib2
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
def driver_open_vv(url):
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36")
    #driver=webdriver.PhantomJS(desired_capabilities={'phantomjs.page.settings.resourceTimeout': '10'})
    #driver=webdriver.PhantomJS()
    driver=webdriver.PhantomJS(executable_path='C:\\Users\\dmdnh\\AppData\\Roaming\\npm\\phantomjs.cmd')
    res1 = driver.get(url)
    html1 = driver.page_source
    html2 = driver.execute_script("return document.documentElement.innerHTML;")
    soup1 = BS(html2)
    os.system('pkill phantomjs')
    return soup1

### using phantomjs to open a website and return the soup value
def driver_open(url):
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36")
    #driver=webdriver.PhantomJS(executable_path='C:\\Users\\dmdnh\\AppData\\Roaming\\npm\\phantomjs.cmd')
    #driver=webdriver.PhantomJS(desired_capabilities={'phantomjs.page.settings.resourceTimeout': '10000'})
    driver=webdriver.PhantomJS()
    from selenium.webdriver import FirefoxOptions
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(firefox_options=opts)
    '''
    binary = FirefoxBinary('/usr/bin/firefox')
    driver=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
    driver=webdriver.Firefox(firefox_binary=binary)
    '''
    res1 = driver.get(url)
    html1 = driver.page_source
    html2 = driver.execute_script("return document.documentElement.innerHTML;")
    soup1 = BS(html2)
    driver.close()
    #os.system('pkill phantomjs')
    return soup1

###
def endswith_yu(url2):
    res2 = urllib2.urlopen(url2)
    soup2=BS(res2)
    return soup2


# write the files
# * issue          is the issue/volume string
# * url            is the link of the paper
# * title       is the title of the paper
# * text           is all the paragraph that is good which
#-- can be loop
def write_file_yu(issue,url,title,text):
    with open(issue+'_text.txt','a') as f:
        f.write(str(url.encode('utf-8'))+"\n\n")
        f.write('main_title  '+str(title.encode('utf-8'))+"\n\n")
        for a1 in text:
            a2_text=a1.getText()
            f.write(str(a2_text.encode('utf-8'))+"\n")

def get_url(soup):
    urls=[]
    a1=soup.findAll("a")
    for aa1 in a1:
        s1=aa1.get("class")
        #print s1
        if type(s1)==list:
            if 'artTitle' in s1:
	            #print s1[1]
                hh1=aa1.get('href')
	            #print hh1
                urls.append(hh1)
    return urls


## some website cannot direct use urlopener to open
# we need to add a head file
def url_opener(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(url)
    #response = urllib2.urlopen(u1)
    #soup_u1 = BS(response)
    soup_u1 = BS(response,'lxml')
    return soup_u1
