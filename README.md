# ExchangeCVESearch
search exchange cve ID

Find the cve id: 
python3 main.py -t 192.168.1.1

Example: 
内部版本号: 15.1.1034 
产品版本号: Microsoft Exchange Server 2016 Cumulative Update 6 
漏洞编号(基于版本的理论扫描): ['CVE-2017-8758', 'CVE-2017-11932', 'CVE-2017-11761'

update "saveVuln.txt":
python3 main.py --update
