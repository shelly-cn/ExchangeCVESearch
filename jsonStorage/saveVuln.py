#encoding=utf-8
import json
import cvePull.pullMitreCVE
import microsoftPull.pullMicrosoftProductName

def save_vuln():
    cveName = cvePull.pullMitreCVE.mitre_pull_cve()
    #保存cveName、productNumber、product到本地文件
    file = open('saveVuln.txt', 'w')
    #建立list存储cveName、productNumber、product
    save = {}
    for cve in cveName:
        productNumber, productName = microsoftPull.pullMicrosoftProductName.microsoft_pull_product_name(cve)
        save['cveName'] = cve
        save['productNumber'] = int(productNumber)
        save['product'] = productName
        #print(save)
        # for i in range(0, int(productNumber)):
        #     save['cveName'] = cve
        #     save['productNumber'] = int(productNumber)
        #     save['product' + str(i)] = productName[i]
        #     print("i==========%s", i)

        # save['cveName'] = cve
        # save['productNumber'] = int(productNumber)
        # for i in range(0, int(productNumber)):
        #     save['product' + str(i)] = productName[i]
        #     print("i==========%s", i)
        # print(save)

        file.write(json.dumps(save,ensure_ascii=True) + "\n")
    file.close()
    