#encoding=utf-8
import urllib3
import requests
from bs4 import BeautifulSoup

def get_owa_version(owaAddr):
    #去除ssl证书告警
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = 'https://' + owaAddr + '/owa/auth/logon.aspx'
    #测试页面
    #url = 'http://' + owaAddr + '/1.html'
    headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    r = requests.get(url, verify=False, headers=headers)
    htmlText = r.text
    soup = BeautifulSoup(htmlText, 'lxml')
    tags = soup.find_all('link')
    for tag in tags:
        hrefVul = tag.get('href')
    #返回类型示例：['', 'owa', 'auth', '15.1.225', 'themes/resources/favicon.ico']
    hrefSplit = hrefVul.split("/", 4)
    ExchangeVersion = hrefSplit[3]
    return ExchangeVersion