#encoding=utf-8
import re
import json
import urllib3
import requests
from bs4 import BeautifulSoup

def microsoft_pull_product_name(cveID):
    productNameList = []
    #去除ssl证书告警
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = "https://api.msrc.microsoft.com/sug/v2.0/en-US/affectedProduct?$filter=cveNumber+eq+'" + cveID + "'"
    headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    r = requests.get(url, verify=False, headers=headers)
    htmlJsonProductCount = json.loads(r.text).get('@odata.count')
    htmlJsonVaule = json.loads(r.text).get('value')
    for value in htmlJsonVaule:
        productNameList.append(value["product"])
    #返回影响产品数量和产品详细名称
    return htmlJsonProductCount, productNameList