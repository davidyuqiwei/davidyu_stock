from bs4 import BeautifulSoup as BS
import os
import urllib.request
import urllib.parse
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

