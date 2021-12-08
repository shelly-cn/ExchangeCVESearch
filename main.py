#encoding=utf-8
import versionJud
import jsonStorage.saveVuln
import versionNumberCompar
import argparse

def main():
    #接收命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', help = 'Example:mail.attack.com')
    parser.add_argument('-u', '--update', dest = 'update', help = 'Update CVE file', action="store_true")
    args = parser.parse_args()
    #接收输入为update执行update cve操作
    if args.update:
        jsonStorage.saveVuln.save_vuln()
        #print("update")
    #接收输入为target或t执行漏洞检测输出操作
    elif args.target == "target" or "t":
        owaAddr = args.target
        intVersion, proVersion = versionJud.judge_version(owaAddr)
        print("\033[1;32;43m内部版本号:\033[0m",intVersion)
        print("\033[1;32;43m产品版本号:\033[0m",proVersion)
        print("\033[1;32;43m漏洞编号(基于版本的理论扫描):\033[0m",versionNumberCompar.version_num_compar(owaAddr))   

if __name__ == "__main__":
    main()