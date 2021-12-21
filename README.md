# ExchangeCVESearch

内部版本号由于太费时间，没有完全匹配完成，可通过Microsoft官网：https://docs.microsoft.com/zh-cn/exchange/new-features/build-numbers-and-release-dates?view=exchserver-2019 进行匹配并写入文件“versionJud.py”的“interShortVersion”字段和“ExchangeProductName”字段，格式按照之前定义好的格式进行写入

search exchange cve ID

Find the cve id: 
python3 main.py -t 192.168.1.1

Example: 
内部版本号: 15.1.1034 
产品版本号: Microsoft Exchange Server 2016 Cumulative Update 6 
漏洞编号(基于版本的理论扫描): ['CVE-2017-8758', 'CVE-2017-11932', 'CVE-2017-11761'

update "saveVuln.txt":
python3 main.py --update
