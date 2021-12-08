#encoding=utf-8
import json
import versionJud

def version_num_compar(owaAddr):
    #定义cve返回list
    cveList = []
    #获取目标的产品名称
    _, proVersion = versionJud.judge_version(owaAddr)
    #读取本地保存的cve对应exchange产品文件中的json数据
    with open("saveVuln.txt", "r", encoding="utf-8") as f:
        #分行读取json数据
        for jsonstr in f.readlines():
            #获取每行json中的cveName、productNumbe、product三个字段的数据信息
            cveName = json.loads(jsonstr).get('cveName')
            productNumber = json.loads(jsonstr).get('productNumber')
            product = json.loads(jsonstr).get('product')
            #判断cve对应的产品名称中产品数量是否大于0，如果为0则跳过
            if int(productNumber) != 0:
                #遍历每个产品
                for i in range(0, int(productNumber)):
                    #用遍历的产品名称和目标产品名称做比对判断，如果相同则输出到cveList中
                    if proVersion == product[i]:
                        cveList.append(cveName)
    return cveList