from bs4 import BeautifulSoup as BS
import os
import urllib.request
import urllib.parse
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
def url_opener(url):
    #opener = urllib2.dbuild_opener()
    #opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    values={'act':'login'}
    req = urllib.request.Request(url,values ,headers)
    response = urllib.request.urlopen(url)
    #response = urllib2.urlopen(u1)
    soup_u1 = BS(response,"html.parser")
    return soup_u1

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

def driver_open_noBS(url):
    from selenium.webdriver import Firefox
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.add_argument('-headless')
    driver = Firefox(executable_path='/usr/local/bin/geckodriver', options=options)
    driver.get(url)
    html1 = driver.page_source
    html2 = driver.execute_script("return document.documentElement.innerHTML;")
    #soup1 = BS(html2)
    driver.close()
    #os.system('pkill phantomjs')
    return html2
