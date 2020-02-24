from bs4 import BeautifulSoup as BS
import os
import urllib.request
import urllib.parse
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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

def driver_open(url,the_encoding = "utf-8",timeout=3):
    from selenium.webdriver import FirefoxOptions
    from selenium import webdriver
    import time
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(firefox_options=opts)
    driver.set_page_load_timeout(timeout)
    #driver.set_script_timeout(3)
    try:
        res1 = driver.get(url)  ## may jumpout timeout error, the js has just finish load, reutrn the innerhtml
    except:
        time.sleep(5)
    finally:
        #time.sleep(5)
        print("++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++ run finnaly +++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++")
        html2 = driver.execute_script("return document.documentElement.innerHTML;")
        soup1 = BS(html2.encode(the_encoding))
        driver.close()
    #os.system('pkill phantomjs')
    return soup1

def driver_open_noBS(url):
    from selenium.webdriver import Firefox
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = Firefox(executable_path='/usr/local/bin/geckodriver', options=options)
    driver.get(url)
    html1 = driver.page_source
    html2 = driver.execute_script("return document.documentElement.innerHTML;")
    driver.close()
    return html2

