#encoding=utf-8
import re
import json
import urllib3
import requests
from lxml import etree
from bs4 import BeautifulSoup

def mitre_pull_cve():
    cveNameList = []
    #去除ssl证书告警
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=Microsoft+Exchange+Server"
    #url = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=Microsoft+Windows+Media+Foundation+Remote+Code+Execution+Vulnerability"
    headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    r = requests.get(url, verify=False, headers=headers)
    #html = r.content.decode('utf-8')
    html = r.text
    bs = BeautifulSoup(html, "html.parser")
    #tags = list(bs.find(id="TableWithRules").table.children)
    div = bs.find('div', {'id':'TableWithRules'})
    tds = div.findAll('td')
    for td in tds:
        try:
            #print(td.a.string)
            cveNameList.append(td.a.string)
        except:
            pass
    return cveNameList