import requests
import argparse
import sys 


def banner():

    banner = '''
______                                  _     
| ___ \                                | |    
| |_/ /__   ___ ___  ___  __ _ _ __ ___| |__  
|  __/ _ \ / __/ __|/ _ \/ _` | '__/ __| '_ \ 
| | | (_) | (__\__ \  __/ (_| | | | (__| | | |
\_|  \___/ \___|___/\___|\__,_|_|  \___|_| |_|
                                                                                         

                  Author : Givemefivw
                  Version: 0.1
                  Descrip: Poc-in-github项目查询脚本，网络不通的情况下需要梯子，查询到CVE编号后访问链接即可                                    
                                                      
    '''
    print(banner)

def monitor(year,cve):
    url = "https://github.com/nomi-sec/PoC-in-GitHub/tree/master/{}".format(year)
    try:
        res = requests.get(url,timeout=2)
        if res.status_code == 200 and 'CVE-{}-{}'.format(year,cve) in res.text:
            print("[+] CVE-{}-{} is in Github".format(year,cve))

            print("[*] https://github.com/nomi-sec/PoC-in-GitHub/blob/master/{}".format(year) + "/CVE-{}-{}.json".format(year,cve))
        else:
            print("[-] CVE-{}-{} is not in Github".format(year,cve))
    except Exception as e:
        print("[-] May be you need VPN ?")
    except KeyboardInterrupt:
        sys.exit()

def main():
    parser = argparse.ArgumentParser(description='Bilibillitrans Help')
    parser.add_argument('-y','--year',help='cve-year',default='')
    parser.add_argument('-c','--cve',help='cve',default='')
    args = parser.parse_args()

    if args.year and args.cve:
        year = args.year
        cve = args.cve
        monitor(year,cve)

if __name__ == '__main__':
    banner()
    main()